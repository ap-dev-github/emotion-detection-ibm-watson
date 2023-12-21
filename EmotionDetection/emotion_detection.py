'''
This file contains a function which
 communicate with the IBM watson nlp emotion 
 predict library and return the response
'''
import requests, json
def emotion_detector(text_to_analyse):
    '''
    This function sends the text which is to be 
    analyzed to the IBM watson nlp library using the post request.
    It received the response and then convert it into the desired 
    dictionary using json library and then extract different emotion
    values from the list of dictionary we get. And also handles if the 
    text_to _analyse is an empty text by returning all the values as 
    none.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response= requests.post(url, json = myobj, headers = header)

    if response.status_code == 400:
        anger_score = None   
        disgust_score = None 
        fear_score = None 
        joy_score = None 
        sadness_score = None 
        dominant_emotion = None         
    else:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        #dictionary to map the emotion_scores to their names
        emotion_mapping = {
        anger_score: 'anger',
        disgust_score: 'disgust',
        fear_score: 'fear',
        joy_score: 'joy',
        sadness_score: 'sadness',
        }
        dominant_score = max(formatted_response['emotionPredictions'][0]['emotion'].values())
        dominant_emotion=emotion_mapping[dominant_score]
    return{
        'anger': anger_score,
        'disgust':disgust_score,
        'fear':fear_score,
        'joy':joy_score,
        'sadness':sadness_score,
        'dominant_emotion':dominant_emotion, }
    

