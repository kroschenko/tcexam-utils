import xml.etree.ElementTree as ET
import random
import argparse


parser = argparse.ArgumentParser(description="F11 fixer for tc-exam testing system")
parser.add_argument(
    "exported_xml",
    help="xml for a exported module",
    type=str,
)
parser.add_argument(
    "fixed_xml",
    help="fixed xml with random order of answers",
    type=str,
)
parser.add_argument(
    "module_new_name",
    help="name of new fixed module",
    type=str,
)

args = parser.parse_args()

tree = ET.parse(args.exported_xml)
root = tree.getroot()

module = root[1].find("module")

module.find("name").text = args.module_new_name
subjects = module.findall("subject")
for subject in subjects:
    questions = subject.findall("question")
    for question in questions:
        answers = question.findall("answer")
        correct_answer = answers[0]
        random_index = random.randint(0, len(answers)-1)
        correct_desc = correct_answer.find("description").text
        correct_flag = correct_answer.find("isright").text
        correct_enabled = correct_answer.find("enabled").text
        correct_answer.find("description").text = answers[random_index].find("description").text
        correct_answer.find("isright").text = answers[random_index].find("isright").text
        correct_answer.find("enabled").text = answers[random_index].find("enabled").text
        answers[random_index].find("description").text = correct_desc
        answers[random_index].find("isright").text = correct_flag
        answers[random_index].find("enabled").text = correct_enabled

tree.write(args.fixed_xml, encoding="UTF-8")

