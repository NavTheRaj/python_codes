import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
#colors=['blue','yellow','black','pink','orange','red']

plt.bar(y_pos, performance, align='center', alpha=0.05)
plt.xticks(y_pos, objects)
plt.xlabel('Languages')
plt.ylabel('Usage')
plt.title('Programming language usage')
#plt.legend(objects,loc=0)

plt.show()
