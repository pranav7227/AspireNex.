Pranav Patil (praanavpatil3717@gmail.com)

 Firstly ,Thank you for providing me with an opportunity to exhibit my skills , I hope my efforts please you.

I have choose the following projects from thr problem statement:
Image captioning AI
Tic Tac Toe AI

Details

1)Tic Tac Toe AI

This project is a web-based Tic Tac Toe game with an AI opponent. The AI uses the Minimax algorithm with Alpha-Beta Pruning for optimal play. The game has three difficulty levels: easy, medium, and hard.

Technologies Used
Flask: Backend server handling game logic and communication.
HTML/CSS: Structuring and styling the web interface.

Algorithms 
Minimax Algorithm: Simulates all possible moves to find the best one, alternating between maximizing (AI) and minimizing (human) players.
Alpha-Beta Pruning: Optimizes the Minimax algorithm by reducing the number of nodes evaluated.

Difficulty Levels:
Easy: AI makes random moves.
Medium: AI alternates between random moves and optimal moves.
Hard: AI uses Minimax with Alpha-Beta Pruning for optimal moves.

Image captioning AI

This project is a web-based application that generates captions for uploaded images using a pre-trained deep learning model. Users can upload images, and the application returns a descriptive caption generated by a Vision-Encoder-Decoder model.

Technologies Used

Flask: Backend server for handling file uploads and rendering templates.
HTML/CSS: Structuring and styling the web interface.
TensorFlow/Keras: Deep learning framework for pre-trained models.
Transformers (Hugging Face): Library for using pre-trained VisionEncoderDecoderModel, ViTFeatureExtractor, and AutoTokenizer.
Pillow: Python Imaging Library (PIL) for image processing.

Algorithm Overview

VisionEncoderDecoderModel: A pre-trained model combining Vision Transformer (ViT) and GPT-2 for image captioning.
ViTFeatureExtractor: Extracts features from images.
AutoTokenizer: Tokenizes the input text and decodes the output text.
Image Processing: Images are processed using Pillow, and features are extracted using ViTFeatureExtractor.
Caption Generation: Captions are generated by passing the extracted features through the VisionEncoderDecoderModel, utilizing an attention mask and a token limit.
