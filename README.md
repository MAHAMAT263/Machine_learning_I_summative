# Medical Q&A Chatbot
## Project Overview
This project implements a domain-specific chatbot designed to answer medical questions using a fine-tuned Transformer model. It integrates a pretrained language model with a user-friendly Flask web interface, enabling interactive querying and real-time responses. The system supports medical education, preliminary self-diagnosis, and information dissemination.

git repo: https://github.com/MAHAMAT263/Machine_learning_I_summative.git 


Demo link: https://drive.google.com/file/d/1kFgNnqoBcCGwNLgf4KrcuBxxujAuZNI3/view?usp=sharing
## Model & Dataset
Dataset
Source:https://www.kaggle.com/datasets/thedevastator/comprehensive-medical-q-a-dataset/data 


Format: CSV with columns Question, Answer, and qtype.


## Preprocessing:


Dropped unnecessary columns (like qtype).


Renamed columns to question and answer to lowercase.


Split into train, validation, and test sets (80/10/10 split).


## The statistic of the data:
Basic Statistics:
       question_length  answer_length
count     16407.000000   16407.000000
mean         50.684952    1303.452673
std          16.926465    1656.694326
min          16.000000       6.000000
25%          38.000000     487.000000
50%          48.000000     890.000000
75%          61.000000    1589.000000
max         191.000000   29046.000000


## The data visualization:



Model 1(t5-small)
Base Model: t5-small from Hugging Face Transformers.


Fine-tuning task: Text-to-Text Generation (Question → Answer).


Training library: transformers.Trainer


Tokenization: Questions formatted as question: <text> with truncation & padding.


Training Details
Epochs: 5


Batch Size: 8


Learning Rate: 3e-4


Evaluation Metric: Validation loss with early stopping


Model saved to: trained_model/


## Evaluation
BLEU Score: Measured n-gram overlap between predicted and reference answers.


ROUGE Score: Assessed recall and overlap of predicted phrases.
Results:
training_loss=1.9142923570473342;

Validation loss =1.761654

BLEU Score: 0.01417268015643343;

ROUGE Score:
rouge1: 0.2954444299839109
rouge2: 0.17994513747772967
rougeL: 0.24441907733375723
rougeLsum: 0.25001687097112446

The  t5-small curve


Model 2(t5-base)
Base Model: t5-base from Hugging Face Transformers.


Fine-tuning task: Text-to-Text Generation (Question → Answer).


Training library: transformers.Trainer


Tokenization: Questions formatted as question: <text> with truncation & padding.


Training Details
Epochs: 5


Batch Size: 4


Learning Rate: 3e-4


Evaluation Metric: Validation loss with early stopping


Model saved to: trained_model/


## Evaluation
BLEU Score: Measured n-gram overlap between predicted and reference answers.


ROUGE Score: Assessed recall and overlap of predicted phrases.
Results:
training_loss=1.328895994300;

Validation loss =1.362294;

BLEU Score:0.014775497443751015;

ROUGE Score:

  rouge1: 0.29295270655428873
  rouge2: 0.17626402178488537
  rougeL: 0.24260774616732578
  rougeLsum: 0.24524357078751008

The  t5-base curve



Note: Scores are relatively low due to the open-ended and complex nature of medical QA.


| Model     | Epochs | Train Loss | Val Loss | BLEU Score |
|-----------|--------|------------|----------|------------|
| T5-small  | 5      | 1.9142923  | 1.761654 | 0.0141726  |
| T5-base   | 5      | 1.328896   | 1.362294 | 0.0147754  |

## The best model: T5-base 

Based on the evaluation metrics, the best performing model is T5-base. It achieved a lower training loss (1.33) and a slightly lower validation loss (1.36) compared to T5-small. Additionally, it produced a higher BLEU score (0.0148 vs. 0.0142), indicating better quality in generated answers. These results suggest that the T5-base model generalizes better and provides more accurate responses for the medical Q&A task.

## Question and answer used to test the model:

Q: what is cancer?

A: Cancer is a disease in which malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues

Q: what is cancer?

A: Cancer is a disease in which malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues of the body. Malignant (cancer) cells form in the tissues

Application Architecture

## Frontend
Built with HTML + Bootstrap.



User interface to input medical questions.



Asynchronous form submission using JavaScript and fetch().



## Backend (Flask)

Python Flask server serves HTML page and handles POST requests.



Uses T5ForConditionalGeneration to predict answers.



Loads tokenizer and model from trained_model/ directory.



Dependencies
flask
transformers
torch
Sentencepiece



## Usage Instructions

Clone the project locally.



Ensure trained_model/ folder contains all required model files.



## Install dependencies:


pip install -r requirements.txt

Python app.y

## Conclusion

This Medical Q&A Chatbot demonstrates how powerful transformer-based models can be leveraged for specialized question-answering tasks. By combining NLP, Flask web development, and an intuitive interface, the chatbot provides a helpful tool for educational or exploratory medical assistance.
