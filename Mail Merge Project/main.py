import os
PLACEHOLDER="[name]"

with open(r"C:\Users\ssc\Desktop\100.days.of.code\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names=names_file.readlines()

with open(r"C:\Users\ssc\Desktop\100.days.of.code\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        path=r"C:\Users\ssc\Desktop\100.days.of.code\Mail Merge Project Start\Output\ReadyToSend"
        output_file_path = os.path.join(path, f"letter_for_{stripped_name}.txt")
        with open(output_file_path,mode="w") as completed_letter:
            completed_letter.write(new_letter)
