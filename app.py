#-------------------------------------------------------------------------------
# Importation des modules

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st
import include as inc
import os
import subprocess
from midi2audio import FluidSynth
from pydub import AudioSegment
#from pydub.playback import play
import fluidsynth

#-------------------------------------------------------------------------------
# Application principale

st.title("JASAC - Jazz Solo Auto Composer")

st.write("""
    ### Exécution de commandes système y compris audio (test)

""")

#output = subprocess.check_output("ls -al", Shell=True)
#st.write(output)

#sortie=os.popen("ls -al").readlines()
#st.write(sortie)

#DEFAULT_GAIN = 0.8

fs = FluidSynth(sound_font="AltoSoft_Vib.sf2")

fs.midi_to_audio("ArtPepper_Anthropology_FINAL__BIS.mid", "output.wav")

sound = AudioSegment.from_wav("output.wav")

louder_sound = sound + 30

louder_sound.export("louder_output.wav", format="wav")

audio1 = open("louder_output.wav", "rb")
st.audio(audio1)






#-------------------------------------------------------------------------------
# Conclusion avec le lien vers les sources sur GitHub

st.markdown("""
    <hr>
""", unsafe_allow_html=True)

inc.espace(2)

st.write("""
    📝 Sources de l'application :
    [https://github.com/pbejian/regression_simple](https://github.com/pbejian/regression_simple)

""")
#-------------------------------------------------------------------------------
