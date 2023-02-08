import cv2
import pytesseract as pts
import openai

# OPEN AI KEY
openai.api_key = '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'

# STORAGE OF DATA
files = []
translation = []
summaries = []

# GET TEXTBOOK PAGES FILE NAMES FROM THE USER
while True:
    inpt = input("If done, enter N\nGive file name: ")
    if inpt == 'N':
        break
    files.append(inpt)

# STORE IMAGE TO TEXT DATA IN THE ARRAY
for i in files:
    try:
        img = cv2.imread(i)
    except:
        print(f"File <{files[i]}> does not exist.")
    translation.append(pts.image_to_string(img))

# CHATGPT MODEL AND PROMPT
model_engine = "text-davinci-003"

for i in translation:

    prompt = f"Can you give a lengthy summary smartly in a bullet point: {i}"

    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summaries.append(completion.choices[0].text)


# for i in translation:
#     print(i, end='\n\n' + '-'*20)

# print('\n'*5)

for i in summaries:
    print(i)
