def my_languages(results):
    return [lang for lang,score in sorted(results.items(), key=lambda x: -x[1]) if results[lang]>=60]



# from operator import itemgetter
# def my_languages(results):
#     return [language for language, score in sorted(results.items(),key=itemgetter(1), reverse=True) if score >= 60]