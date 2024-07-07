# fuzzy-octo-waffle
do you know what words of yours mean to anybody?
Simple ML system - application, that uses pre-trained BiLSTM NN models, trained on English and self-created Ukrainian datasets.


Built for bachelor diploma work, this repository offers potential users a simple ML application, using both common approaches of its realization:
- Using Google Colaboratory as the main application version, offering the potential user to use their Google account and resources of Google to train, validate, and use their emotion analysis models in this system.
- Using the local version, with interface implementation by Gradio. Unlike Google Colaboratory, you cannot train your models, only use pre-trained or trained by colab notebooks from the main version.

INSTALLATION:
Local Version:
- Download this repo as an archive and extract it to the desired spot on your PC;
- Open the folder and run the "Install.bat" file to execute the installation of all required libs;
- After successful installation - run "launch_main.bat" and then wait until it launches port for Gradio: http://127.0.0.1:7860/
Colab Version:
- Download this repo as an archive and extract it to the desired spot on PC;
- Download to your Google Drive 3 files from folder "colab";
- Open them and follow the instructions for usage.

DATASETS:
For the English emotion analysis model, I had used the next dataset:
https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp

For Ukrainian emotion analysis model, I had created by myself dataset, that consists of 200k+ marked words "negative"/"positive". You can use created dataset and mark me in your project.

I'M OPEN FOR QUESTIONS, REQUESTS, PROPOSITIONS AND CONTRIBUTIONS.
