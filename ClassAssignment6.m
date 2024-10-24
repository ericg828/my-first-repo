pyversion
%for me 'C:\Users\shamu\AppData\Local\Programs\Python\Python312'
mylist = py.list({'apple', 'banana', 'orange', 'pear', 'mango'});
len_of_list = py.len(mylist);
disp(len_of_list);

py_math = py.importlib.import_module('math');
result = py_math.remainder(100,7);
disp(result);

my_str = 'Assignment is done.';
reversed_str = py.str(my_str(end:-1:1));
disp(reversed_str);