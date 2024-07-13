# solving unbalanced dataset problem using ydata_synthetic.synthesizers
from ydata_synthetic.synthesizers import ModelParameters, TrainParameters
from ydata_synthetic.synthesizers.regular import RegularSynthesizer
import pandas as pd

def generate_data():
    ctgan_args = ModelParameters(batch_size=500, lr=5e-4, betas=(0.5, 0.9), noise_dim=32, layers_dim=128)
    train_args = TrainParameters(epochs=40)

    # Train the generator model
    synth = RegularSynthesizer(modelname='ctgan', model_parameters=ctgan_args)    
    return synth, train_args
    
def synthetic_data_model(model_dir, model):
    model = RegularSynthesizer.load(model_dir + model)
    return model

def patient_id_and_date(df):
    df = df.reset_index()
    df.rename(columns={'index': 'patient_id'}, inplace=True)
    df["datetime"] = pd.to_datetime('today')

    return df 