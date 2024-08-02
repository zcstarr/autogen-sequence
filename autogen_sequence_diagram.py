import json
import argparse
import subprocess
from plantuml import PlantUML


def parse_log_file(filename):
    with open(filename, 'r') as file:
        log_lines = file.readlines()

    events = []
    for line in log_lines:
        try:
            event = json.loads(line)
            if 'event_name' in event:
                events.append(event)
        except json.JSONDecodeError:
            continue
    return events


def escape_plantuml_chars(text):
    """
    Escapes problematic characters for PlantUML.
    """
    replacements = {
        '"': '\\"',
        '\\': '\\\\',
        '\n': '\\n',
        '\r': '\\r',
        "'": "\\'"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def generate_plantuml_script(events):
    plantuml_script = "@startuml\n"

    # Add participants
    participants = set()
    for event in events:
        participants.add(event['source_name'])
    for participant in participants:
        plantuml_script += f"participant {participant}\n"

    # Add events
    for event in events:
        if event['event_name'] == 'received_message':
            json_state = json.loads(event['json_state'])
            sender = json_state['sender']
            message = escape_plantuml_chars(json_state['message'])
            plantuml_script += f"{sender} -> {
                event['source_name']}: {message}\n"
        elif event['event_name'] == 'reply_func_executed':
            json_state = json.loads(event['json_state'])
            reply_func_name = escape_plantuml_chars(
                json_state['reply_func_name'])
            plantuml_script += f"{event['source_name']
                                  } -> {event['source_name']}: {reply_func_name}\n"

    plantuml_script += "@enduml"
    return plantuml_script


def save_plantuml_script(script, output_file):
    with open(output_file, 'w') as file:
        file.write(script)


def generate_sequence_diagram_remote(plantuml_script, output_image):
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
    response = server.processes(plantuml_script)
    response.save(output_image)


def generate_sequence_diagram_local(output_script, output_image):
    try:
        subprocess.run(['plantuml', output_script, '-o', output_image])
    except FileNotFoundError:
        print("PlantUML is not installed locally. Please install PlantUML or use the remote option.")


def main():
    parser = argparse.ArgumentParser(
        description='Generate a sequence diagram from log data.')
    parser.add_argument('filename', type=str, help='The log file to process.')
    parser.add_argument('--output-script', type=str,
                        default='sequence_diagram.puml', help='The output PlantUML script file.')
    parser.add_argument('--output-image', type=str,
                        default='sequence_diagram.png', help='The output image file.')
    parser.add_argument('--no-image', action='store_true',
                        help='Only generate the PlantUML script without generating the image.')
    parser.add_argument('--local', action='store_true',
                        help='Generate the sequence diagram locally.')

    args = parser.parse_args()

    events = parse_log_file(args.filename)
    plantuml_script = generate_plantuml_script(events)
    save_plantuml_script(plantuml_script, args.output_script)

    if not args.no_image:
        if args.local:
            generate_sequence_diagram_local(
                args.output_script, args.output_image)
        else:
            generate_sequence_diagram_remote(
                plantuml_script, args.output_image)

    print(f"PlantUML script saved to {args.output_script}")
    if not args.no_image:
        print(f"Sequence diagram image saved to {args.output_image}")


if __name__ == "__main__":
    main()
