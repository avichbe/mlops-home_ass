from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


class ModelLoad():
    
    def load_model() -> pipeline:
        try:
            # Load SecureBert-NER model and tokenizer
            model_name = "CyberPeace-Institute/SecureBERT-NER"
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForTokenClassification.from_pretrained(model_name)
            # model_name = "CyberPeace-Institute/SecureBERT-NER"
            # nlp = pipeline("ner", model=model_name)

            pipeline_ner = pipeline("ner", model=model, tokenizer=tokenizer)
            return pipeline_ner
        
        except Exception as e:
            #log now console
            print(f'cant load model - e is {e}')
