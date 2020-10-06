test = 'filename'
test2 = {
    '1': [2,3,45],
    '2': 'testando'
}
f = open('./Logs/BasicImplementation/byIteration/'+test+'.txt', 'xt')

f.write('testing \n')
f.write('   IT really works')
f.write(str(test2))