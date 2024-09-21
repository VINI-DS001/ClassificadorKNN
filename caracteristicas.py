import os
import cv2
import numpy as np

# Função para carregar imagens e extrair características
def extrair_caracteristicas(dataset_path):
    # Listas para armazenar as características e os rótulos
    caracteristicas = []
    labels = []
    
    # Percorre todos os arquivos no diretório
    for file_name in os.listdir(dataset_path):
        # Verifica se o arquivo é uma imagem
        if file_name.endswith(".jpg"):
            # Caminho completo da imagem
            file_path = os.path.join(dataset_path, file_name)
            
            # Carrega a imagem e converte para tons de cinza
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            
            # Redimensiona a imagem (garantir que todas têm 136x102)
            img_resized = cv2.resize(img, (102, 136))
            
            # Achata a imagem em um vetor de características
            img_flattened = img_resized.flatten()
            
            # Adiciona as características e o rótulo à lista
            caracteristicas.append(img_flattened)
            
            # Define o rótulo com base no nome do arquivo
            if "boot" in file_name:
                labels.append(0)  # 0 para Boot
            elif "Sandal" in file_name:
                labels.append(1)  # 1 para Sandal
            elif "Shoe" in file_name:
                labels.append(2)  # 2 para Shoe
    
    # Converte as listas em arrays numpy
    caracteristicas = np.array(caracteristicas)
    labels = np.array(labels)
    
    return caracteristicas, labels

# Caminho dos datasets (substitua pelos seus caminhos locais)
datasets = {
    "Boot": "Shoe vs Sandal vs Boot Dataset/Boot",
    "Sandal": "Shoe vs Sandal vs Boot Dataset/Sandal",
    "Shoe": "Shoe vs Sandal vs Boot Dataset/Shoe"
}

# Inicializa listas para armazenar todas as características e labels
all_caracteristicas = []
all_labels = []

# Para cada dataset, extrai as características
for dataset_name, dataset_path in datasets.items():
    print(f"Extraindo características de {dataset_name}...")
    carac, labels = extrair_caracteristicas(dataset_path)
    all_caracteristicas.append(carac)
    all_labels.append(labels)

# Concatena todas as características e labels
all_caracteristicas = np.vstack(all_caracteristicas)
all_labels = np.concatenate(all_labels)

print(f"Total de características extraídas: {all_caracteristicas.shape}")
print(f"Total de labels: {all_labels.shape}")
