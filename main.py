from classifai.vectorisers import HuggingFaceVectoriser

vectoriser = HuggingFaceVectoriser(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
