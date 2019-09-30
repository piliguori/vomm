import vomm

training_data = [[1,5,6,7,18],[1,6,7,15,30],[2,3,4,5]]
observed_sequence = [1,2,2,3,4,50]

flat_list = [item for sublist in training_data for item in sublist ]
alphabet_size = max( max(flat_list) + 1, max(observed_sequence) +1 )


my_model = vomm.ppm()
my_model.fit(training_data, d=2, alphabet_size=alphabet_size)

print(my_model.logpdf(observed_sequence))
print(my_model.pdf(observed_sequence))

