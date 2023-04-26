import modules.prepocess as pp
import modules.generate as gen
import multiprocessing


def wordify(file, filepath, wordarts_path):
    try:
        text = pp.extract_text(filepath)
        text = pp.clean_text(text)
        words = pp.process_text(text)
        # print(words)
        wordlist, top_ten_kw = gen._keywords(words)
    except Exception:
        return {"message": "There was an error while generating keywords"}
        
    try:
        wordart = gen._wordart(wordlist)
        wordart_name = file.filename.split('.')[0] + '.png'
        wordart.to_file(wordarts_path + wordart_name)
    except Exception:
        return {"message": "There was an error while generating wordart"}


    return wordart_name, top_ten_kw

