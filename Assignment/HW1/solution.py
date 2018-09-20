# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataScience - COMP4993
# Assignment - 1 


PHONE_DATA = 'phone_data.csv'


class Table(object):
	"""docstring for CSVTable"""
	def __init__(self, header = [], rows = [], data_file = None):

		self.header = header
		self.rows = rows
		self.columns = {}

		if data_file:
			self.load_data_file(data_file)

		self.load_columns()



	def load_data_file(self, data_file):

		f = open(data_file)
		self.header = f.readline().strip().split(',')

		for line in f:
			index,date,duration,item,month,network,network_type = f.readline().strip().split(',')

			index = int(index)
			#date1 = date.split(' ')[0]
			duration = float(duration) 

			self.rows.append([index,date,duration,item,month,network,network_type])
		f.close()

	def load_columns(self):
		
		for i,head in enumerate(self.header):
			self.columns[i] = []

		for row in self.rows:
			for i,elem in enumerate(row):
				self.columns[i].append(elem)


	def filter(self, filter_by):

		filtered_row = []

		for row in self.rows:
			row_live = True
			for key in filter_by:
				ind = self.header.index(key)
				filter_func = filter_by[key]

				if filter_func(row[ind]) == False:
					row_live = False
					break


			if row_live:
				filtered_row.append(row)


		return Table(self.header, filtered_row)



	def group_by(self, column):

		tables = {}
		groups = {}
		ind = self.header.index(column)

		for row in self.rows:
			val = row[ind]

			if column == 'date':
				if val.split(' ')[0] in groups:
					groups[val.split(' ')[0]].append(row)
				else:
					groups[val.split(' ')[0]] = [row,]

			else:
				if val in groups:
					groups[val].append(row)
				else:
					groups[val] = [row,]


		for group in groups:
			tables[group] = Table(self.header,groups[group])

		return tables


	def show(self):
		row_format ="{:>15}" * (len(self.header) + 1)
		print(row_format.format("", *self.header))
		for row in self.rows:
			print(row_format.format('', *row))



	def get_longest_phone_call(self):
		ind = self.header.index('duration')
		longest_call =  max(self.columns[ind])

		ans_table = self.filter({'item': lambda x: x == 'call' ,'duration': lambda x: x == longest_call})
		#print(ans_table.rows)
		return ans_table

	def get_shortest_phone_call(self):
		ind = self.header.index('duration')
		shortest_call =  min(self.columns[ind])

		ans_table = self.filter({'item': lambda x: x == 'call' ,'duration': lambda x: x == shortest_call})
		#print(ans_table.rows)
		return ans_table

			
	def get_phone_calls_massages_of_each_network(self):

		tables = self.group_by('network')
		nhead = ['network', 'phone_calls','sms']
		nrow = []

		for table in tables:
			ftable1 = tables[table].filter({'item': lambda x: x == 'call'})
			ftable2 = tables[table].filter({'item': lambda x: x == 'sms'})
			#print(table, len(ftable.rows))
			nrow.append([table, len(ftable1.rows), len(ftable2.rows)])

		return Table(nhead, nrow)


	def get_longest_phone_call_of_each_network(self):

		tables = self.group_by('network')
		nrow = []
		for table in tables:
			nrow = nrow + Table.get_longest_phone_call(tables[table]).rows

		return Table(self.header, nrow)


	def get_most_phone_call_month(self):

		tables = self.group_by('month')

		max_month = None
		max_count = 0

		for table in tables:
			ftable = tables[table].filter({'item': lambda x: x == 'call'})
			
			if max_count < len(ftable.rows):
				max_month = table
				max_count = len(ftable.rows)

		#print(max_month,max_count)
		nhead = ['month', 'call count']
		nrows = [[max_month, max_count],]
		return Table(nhead,nrows)

	def get_most_massages_month(self):

		tables = self.group_by('month')

		max_month = None
		max_count = 0

		for table in tables:
			ftable = tables[table].filter({'item': lambda x: x == 'sms'})
			
			if max_count < len(ftable.rows):
				max_month = table
				max_count = len(ftable.rows)

		nhead = ['month', 'sms count']
		nrows = [[max_month, max_count],]
		return Table(nhead,nrows)


	def get_most_phone_call_day(self):

		tables = self.group_by('date')

		max_day = None
		max_count = 0

		for table in tables:
			ftable = tables[table].filter({'item': lambda x: x == 'call'})
			
			if max_count < len(ftable.rows):
				max_day = table
				max_count = len(ftable.rows)

		nhead = ['Day', 'call count']
		nrows = [[max_day, max_count],]
		return Table(nhead,nrows)


	def get_most_massage_day(self):

		tables = self.group_by('date')

		max_day = None
		max_count = 0

		for table in tables:
			ftable = tables[table].filter({'item': lambda x: x == 'sms'})
			
			if max_count < len(ftable.rows):
				max_day = table
				max_count = len(ftable.rows)

		nhead = ['Day', 'sms count']
		nrows = [[max_day, max_count],]
		return Table(nhead,nrows)



	def get_phn_call_msg_in_each_network_month(self):
		tables = self.group_by('network')
		nhead = ['network', 'month', 'calls', 'sms']
		nrows = []
		for table in tables:
			ftables = tables[table].group_by('month')

			for ftable in ftables:
				ptable = ftables[ftable].filter({'item': lambda x: x == 'call'})
				mtable = ftables[ftable].filter({'item': lambda x: x == 'sms'})

				#print(table,ftable,len(ptable.rows),len(mtable.rows))
				nrows.append([table,ftable,len(ptable.rows),len(mtable.rows),])

			#print()
			nrows.append(["","","",""])


		return Table(nhead,nrows)



		

if __name__== "__main__":
  
	table = Table([], [], PHONE_DATA)
	print("")
	print("(1) What are the longest phone calls?:")
	table.get_longest_phone_call().show()

	print("")

	print("(1) What are the shortest phone calls?:")
	table.get_shortest_phone_call().show()

	print("")

	print("(2) (A) How many phone calls of each network?")
	print("(2) (A) How many messages of each network?")     
	table.get_phone_calls_massages_of_each_network().show()

	print("")

	print("(3) What are the longest phone calls of each network?")
	table.get_longest_phone_call_of_each_network().show()

	print("")

	print("(4) (A) Which month has the most number of phone calls?")
	table.get_most_phone_call_month().show()

	print("(4) (B) Which month has the most number of messages?")
	table.get_most_massages_month().show()

	print("")

	print("(5) (A) Which day has the most number of phone calls")
	table.get_most_phone_call_day().show()

	print("")

	print("(5) (B) Which day has the most number of messages?")
	table.get_most_massage_day().show()

	print("")

	print("(6) How many phone calls and messages of each network in each month?")
	table.get_phn_call_msg_in_each_network_month().show()

