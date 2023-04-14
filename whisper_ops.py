import whisper

base_model = whisper.load_model("base")


def transcribe_to_text(file):
    try:
        result = base_model.transcribe(file.name, fp16=False, language='ru')
        transcribed_text = result.get("text")
    except Exception as e:
        return("Found error in work with wisper")

    if transcribed_text is None:
        return "Audio could not be transcribed"

    # ответ whisper по умолчанию, если был задан пустой файл
    empty_var = " Редактор субтитров А.Семкин Корректор А.Егорова"
    if ( (len(transcribed_text) == 0) or (transcribed_text == empty_var) ):
        return "Audio is emtpy"

    return transcribed_text
