from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

from django.shortcuts import render

def add(request):
	from random import randint
	num_1 = randint(0,12)
	num_2 = randint(0,12)
	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if no form fillout
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			color = 'warning'
			return render(request, 'add.html', {
			'color':color,
			'my_answer': my_answer,
			'answer':answer,
			'num_1': num_1,
			'num_2': num_2, 
			})

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " +" + old_num_2 + "=" + answer
			color = "success"
		else:
			my_answer = "Incorrect! " + old_num_1 + " +" + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger"
		return render(request, 'add.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2, 
			'color': color,
			})
	return render(request, 'add.html', {
		'num_1': num_1,
		'num_2': num_2, 
		})

from django.shortcuts import render

def subtract(request):
	from random import randint
	num_1 = randint(0,12)
	num_2 = randint(0,12)

	#generate a new pair of cards while num_1 is less that num_2
	temp_answer = int(num_1) - int(num_2)
	while temp_answer < 0: 
		num_1 = randint(0,12)
		num_2 = randint(0,12)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if no form fillout
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			color = 'warning'
			return render(request, 'subtract.html', {
			'color':color,
			'my_answer': my_answer,
			'answer':answer,
			'num_1': num_1,
			'num_2': num_2, 
			})
		
		correct_answer = int(old_num_1) - int(old_num_2)

		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " -" + old_num_2 + "=" + answer
			color = "success"
		else:
			my_answer = "Incorrect! " + old_num_1 + " -" + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger"
		return render(request, 'subtract.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2, 
			'color': color,
			})
	return render(request, 'subtract.html', {
		'num_1': num_1,
		'num_2': num_2, 
		})


from django.shortcuts import render

def multiply(request):
	from random import randint
	num_1 = randint(0,12)
	num_2 = randint(0,12)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if no form fillout
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			color = 'warning'
			return render(request, 'multiply.html', {
			'color':color,
			'my_answer': my_answer,
			'answer':answer,
			'num_1': num_1,
			'num_2': num_2, 
			})


		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " * " + old_num_2 + "=" + answer
			color = "success"
		else: 
			my_answer = "Incorrect! " + old_num_1 + " * " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger"
		return render(request, 'multiply.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2, 
			'color': color,
			})
	return render(request, 'multiply.html', {
		'num_1': num_1,
		'num_2': num_2, 
		})


from django.shortcuts import render

def divide(request):
	from random import randint
	num_1 = randint(0,12)
	num_2 = randint(1,12)

	#generate a new pair of cards while division is not exact giving a remainder
	remainder = int(num_1) % int(num_2)
	while (remainder > 0): 
		num_1 = randint(0,12)
		num_2 = randint(1,12)
		remainder = int(num_1) % int(num_2)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if no form fillout
		if not answer:
			my_answer = "Hey! You forgot to fill out the form!"
			color = 'warning'
			return render(request, 'divide.html', {
			'color':color,
			'my_answer': my_answer,
			'answer':answer,
			'num_1': num_1,
			'num_2': num_2, 
			})

		correct_answer = int(old_num_1) / int(old_num_2)
		if int(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + "=" + answer 
			color = "success"
		else: 
			my_answer = "Incorrect! " + old_num_1 + " / " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
			color = "danger"
		return render(request, 'divide.html', {
			'answer':answer,
			'my_answer': my_answer,
			'num_1': num_1,
			'num_2': num_2, 
			'color': color,
			})
	return render(request, 'divide.html', {
		'num_1': num_1,
		'num_2': num_2, 
		})