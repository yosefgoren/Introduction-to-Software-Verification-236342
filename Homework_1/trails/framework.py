import numpy as np
from time import sleep
from enum import Enum
from matplotlib import pyplot as plt
from threading import Thread
from tqdm import tqdm
# Details on these threads at: https://docs.python.org/3/library/threading.html


class ResultOutput:
	def __init__(self, finished: bool, result = None):
		self.finished = finished
		self.result = result

class ResultType(Enum):
	Success = 1
	Fail = 2
	Unfinished = 3
	NotApplied = 4
	
	def color(self):
		if self == ResultType.Success:
			return 'green'
		elif self == ResultType.Fail:
			return 'red'
		elif self == ResultType.Unfinished:
			return 'yellow'
		elif self == ResultType.NotApplied:
			return 'blue'
		else:
			raise Exception('Invalid ResultType')

	def __str__(self):
		if self == ResultType.Success:
			return 'Success'
		elif self == ResultType.Fail:
			return 'Fail'
		elif self == ResultType.Unfinished:
			return 'Unfinished'
		elif self == ResultType.NotApplied:
			return 'Not Applied'
		else:
			raise Exception('Invalid ResultType')

class Result:
	def __init__(self, type: ResultType, x, y):
		self.type = type
		self.x = x
		self.y = y

class Reference:
	def __init__(self):
		self.obj = "reference to nothing!"

def runAndStore(store: Reference, func, func_args):
	try:
		store.obj = func(*func_args)
	except RecursionError as e:
		# print("run finished due to recursion error")
		store.obj = None
	# print(f"\tfinished running {func.__name__}{func_args} and got {store.obj}")

def tryRunBounded(func, func_args, time_limit_seconds = 1)->ResultOutput:
	output = Reference()
	# print("starting thread")
	t = Thread(target=runAndStore, args=(output, func, func_args))
	t.daemon = True
	t.start()
	sleep(time_limit_seconds)
	# print("finished sleeping")
	if t.is_alive():
		# print("thread did not finish")
		return ResultOutput(False)
	# print("thread finished")
	if(output.obj == None):
		return None
	return ResultOutput(True, output.obj)

def runGrid(target_func, pre_condition, post_condition, n = 3, time_limit_seconds = 1, override_points = None):
	if override_points is None:
		xs, ys = np.meshgrid(np.linspace(-n, n, 2*n+1), np.linspace(-n, n, 2*n+1))
		xs, ys = xs.flatten(), ys.flatten()
	else:
		xs, ys = override_points

	# print(f"{xs=}, {ys=}")
	results = []
	
	print("Running experiments...")
	for i in tqdm(range(len(xs))):
		x = xs[i]
		y = ys[i]
		if not pre_condition(x,y):
			results.append(Result(ResultType.NotApplied, x, y))
			continue
		#allow up to time_limit seconds to run:
		result = tryRunBounded(target_func, (x,y), time_limit_seconds)
		if result is None:
			results.append(Result(ResultType.Unfinished, x, y))
		elif not result.finished:
			results.append(Result(ResultType.Unfinished, x, y))
		elif post_condition(*result.result):
			results.append(Result(ResultType.Success, x, y))
		else:
			results.append(Result(ResultType.Fail, x, y))
	return results

def plotResults(list_of_results: list):
	fig, ax = plt.subplots()
	all_lists = [success, fail, unfinished, not_applied] = [([], []), ([], []), ([], []), ([], [])]
	all_types = [ResultType.Success, ResultType.Fail, ResultType.Unfinished, ResultType.NotApplied]
	
	for r in list_of_results:
		if r.type == ResultType.Success:
			success[0].append(r.x)
			success[1].append(r.y)
		elif r.type == ResultType.Fail:
			fail[0].append(r.x)
			fail[1].append(r.y)
		elif r.type == ResultType.Unfinished:
			unfinished[0].append(r.x)
			unfinished[1].append(r.y)
		elif r.type == ResultType.NotApplied:
			not_applied[0].append(r.x)
			not_applied[1].append(r.y)
		else:
			raise Exception('Invalid ResultType')
	
	print("Plotting results...")
	for i in tqdm(range(len(all_lists))):
		ls = all_lists[i]
		list_type_class = all_types[i]
		ax.scatter(ls[0], ls[1], color=list_type_class.color(), label=str(list_type_class))
	plt.legend()
	plt.show()