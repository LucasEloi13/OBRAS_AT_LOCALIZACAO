from app.config import UPLOAD_FOLDER, ICON_PATH
from app.data_processing import load_and_process_data
from app.map_generation import generate_map

def main():
    file_path = f"{UPLOAD_FOLDER}/tabela_locacao.xlsx"
    gdf = load_and_process_data(file_path)
    mapa = generate_map(gdf, ICON_PATH)
    mapa.save('templates/meu_mapa.html')

if __name__ == "__main__":
    main()
