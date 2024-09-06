import torch
import time



def simple_prediction(pipeline,text) -> str:
    try:
        if text:
            start_time = time.perf_counter()
            # Tokenize input text
            tokens = pipeline.tokenizer(text, return_tensors="pt")
    
            # Run the model and get predictions
            with torch.no_grad():
                outputs = pipeline.model(**tokens)
                logits = outputs.logits
                predictions = torch.argmax(logits, dim=-1).squeeze().tolist()
    
            # Convert predictions to entity labels
            label_map = pipeline.model.config.id2label
            predicted_entities = [label_map[pred] for pred in predictions]
    
            # Tokenize input text to align with predictions
            tokenized_words = pipeline.tokenizer.convert_ids_to_tokens(tokens['input_ids'].squeeze().tolist())
    
            # Return entities and corresponding words
            result = [{"word": word, "entity": entity} for word, entity in zip(tokenized_words, predicted_entities)]
            #write to log for performance test
            print(f'time to prediction is - {time.perf_counter() - start_time:2f} ms')
            return result
        else:
            raise Exception('text is empty')
    except Exception as e:
        print(f'problem with bl  exce is: {e}')