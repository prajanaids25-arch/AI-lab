import numpy as np
from hmmlearn import hmm
# Define the HMM parameters
states = ["Rainy", "Sunny"]
n_states = len(states)
observations = ["Walk", "Shop", "Clean"]
n_observations = len(observations)
# Start probability
start_probability = np.array([0.6, 0.4])
# Transition probability matrix
transition_probability = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])
# Emission probability matrix
emission_probability = np.array([
    [0.1, 0.4, 0.5],
    [0.6, 0.3, 0.1]
])
# Create the HMM model
model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability
# Define a sequence of observations
observed_sequence = np.array([[0], [1], [2]])  # Corresponds to "Walk", "Shop", "Clean"
# Fit the model to the data
model.fit(observed_sequence)
# Predict the hidden states
logprob, hidden_states = model.decode(observed_sequence, algorithm="viterbi")
print("\nObserved sequence:", [observations[i[0]] for i in observed_sequence])
print("\nPredicted hidden states:", [states[i] for i in hidden_states])
print("\nLog probability of the observed sequence:", logprob)
