from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from caracteristicas import all_caracteristicas, all_labels
import cv2
import os
import numpy as np

# Divisão dos dados em treino e validação (80% treino, 20% validação)
X_train, X_val, y_train, y_val = train_test_split(all_caracteristicas, all_labels, test_size=0.2, random_state=42)

# Inicializa o classificador KNN (vamos começar com k=3, que você pode ajustar depois)
knn = KNeighborsClassifier(n_neighbors=3)

# Treina o classificador nos dados de treino
print("Treinando o classificador KNN...")
knn.fit(X_train, y_train)

# Faz a predição nos dados de validação
y_pred = knn.predict(X_val)

# Avalia o desempenho no conjunto de validação
print("Desempenho no conjunto de validação:")
print(classification_report(y_val, y_pred, target_names=["Boot", "Sandal", "Shoe"]))
print(f"Acurácia: {accuracy_score(y_val, y_pred):.4f}")

# Função para carregar e prever as classes de imagens de teste
def classificar_imagens_teste(test_path):
    # Percorre a pasta de imagens de teste
    for file_name in os.listdir(test_path):
        if file_name.endswith(".jpg"):
            file_path = os.path.join(test_path, file_name)
            
            # Carrega a imagem, converte para tons de cinza e redimensiona
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            img_resized = cv2.resize(img, (102, 136))
            img_flattened = img_resized.flatten().reshape(1, -1)  # Transforma em vetor

            # Faz a predição
            prediction = knn.predict(img_flattened)
            
            # Mapeia o rótulo predito para a classe correspondente
            label_map = {0: "Boot", 1: "Sandal", 2: "Shoe"}
            pred_class = label_map[prediction[0]]
            
            print(f"Imagem {file_name} classificada como: {pred_class}")

# Caminho para a pasta de imagens de teste (substitua pelo caminho da sua pasta)
test_images_path = "Imagens de Teste"

# Classifica as imagens de teste
classificar_imagens_teste(test_images_path)
