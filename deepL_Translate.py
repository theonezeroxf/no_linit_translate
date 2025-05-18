# reference https://github.com/DeepLcom/deepl-python
auth_key='60f4d7ab-7fee-4e57-b475-eb2feb2879c4:fx'

import deepl
def example_simple():

    auth_key = "f63c02c5-f056-..."  # Replace with your key
    translator = deepl.Translator(auth_key)

    result = translator.translate_text("Hello, world!", target_lang="FR")
    print(result.text)  # "Bonjour, le monde !"

def example_translate_str():
    # Translate text into a target language, in this case, French:
    result = translator.translate_text("Hello, world!", target_lang="FR")
    print(result.text)  # "Bonjour, le monde !"

    # Translate multiple texts into British English
    result = translator.translate_text(
        ["お元気ですか？", "¿Cómo estás?"],
        target_lang="EN-GB",
    )
    print(result[0].text)  # "How are you?"
    print(result[0].detected_source_lang)  # "JA" the language code for Japanese
    print(result[0].billed_characters)  # 7 - the number of characters in the source text "お元気ですか？"
    print(result[1].text)  # "How are you?"
    print(result[1].detected_source_lang)  # "ES" the language code for Spanish
    print(result[1].billed_characters)  # 12 - the number of characters in the source text "¿Cómo estás?"

    # Translate into German with less and more Formality:
    print(
        translator.translate_text(
            "How are you?", target_lang="DE", formality="less"
        )
    )  # 'Wie geht es dir?'
    print(
        translator.translate_text(
            "How are you?", target_lang="DE", formality="more"
        )
    )  # 'Wie geht es Ihnen?'

def example_translate_file():
    # Translate a formal document from English to German
    input_path = "/path/to/Instruction Manual.docx"
    output_path = "/path/to/Bedienungsanleitung.docx"
    try:
        # Using translate_document_from_filepath() with file paths 
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang="DE",
            formality="more"
        )

        # Alternatively you can use translate_document() with file IO objects
        with open(input_path, "rb") as in_file, open(output_path, "wb") as out_file:
            translator.translate_document(
                in_file,
                out_file,
                target_lang="DE",
                formality="more"
            )

    except deepl.DocumentTranslationException as error:
        # If an error occurs during document translation after the document was
        # already uploaded, a DocumentTranslationException is raised. The
        # document_handle property contains the document handle that may be used to
        # later retrieve the document from the server, or contact DeepL support.
        doc_id = error.document_handle.id
        doc_key = error.document_handle.key
        print(f"Error after uploading ${error}, id: ${doc_id} key: ${doc_key}")
    except deepl.DeepLException as error:
        # Errors during upload raise a DeepLException
        print(error)

def test():
    translator = deepl.Translator(auth_key)
    result = translator.translate_text("Vincent woke up frowning. The cry of a newborn baby was heard in the quiet mountain where even the birds slept.", target_lang="ZH-HANS")
    print(result.text)  # 文森特皱着眉头醒来。在连鸟儿都沉睡的宁静山林中，传来了新生婴儿的啼哭声。

def test2():
    input_path='D:\code\Translate\InfinityMageNovel-main\Infinity Mage Volumes 1-51 Translated\Infinity Mage Volume 05.txt'
    output_path='D:\code\Translate\InfinityMageNovel-main\cn\Infinity Mage Volume 05.txt'
    translator = deepl.Translator(auth_key)
    translator.translate_document_from_filepath(
        input_path,
        output_path,
        target_lang="ZH-HANS",
    )
    print('\n%s translate completed!\n Saved in %s'%(input_path,output_path))
if __name__=="__main__":
    test2()