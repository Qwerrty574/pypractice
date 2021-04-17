from sklearn.preprocessing import MinMaxScaler
import os
import pandas as pd

directory = './directorie/'  # папка с файлами

# files_name=os.listdir(directory)
# files = [os.path.join(directory,f) for f in files_name]
f = os.path.join(directory, 'pima-indians-diabetes.csv')

data = pd.read_csv(f, sep=',')  # , , na_values=' ')
# data.columns = ['A' + str(i) for i in range(1, 25)] +['Label']
data.columns = ['A' + str(i) for i in range(1, 9)] + ['class']

data.at[data['class'] == 2, 'class'] = 0  # нет заболевания (редкие)
data.at[data['class'] == 1, 'class'] = 1  #

# data=data.rename(columns={'Label':'class'})


# data= pd.read_csv(f,sep=';',header=None,na_values=' ')

X_first_format = data.drop(('class'), axis=1)  # Выбрасываем столбец 'class'.

# data.at[data['class']=='NRB','class']=0 #отсутствие заболевания +1
# data.at[data['class']=='RB','class']=1 # наличие -1


# data_1_tr, data_1_te=train_test_split(data[data['class']==1] , test_size=0.1, random_state=rn_split)
# data=pd.concat([data[data['class']==0], data_1_te], axis=0)

X_first_format = data.drop(('class'), axis=1)  # Выбрасываем столбец 'class'.
# imp = SimpleImputer(missing_values=np.nan, strategy='mean')
# imp.fit(X_first_format)
# train_X_first_format = imp.transform(X_first_format)

# min_max_scaler=preprocessing.MinMaxScaler()
# X=min_max_scaler.fit_transform(train_X_first_format)

# ВНИМАТЕЛЬНО!!!!!!!!
y = data['class']
# scaler=StandardScaler()
# X = pd.DataFrame(scaler.fit_transform(X_first_format))
scaler = MinMaxScaler()
X = pd.DataFrame(scaler.fit_transform(X_first_format))
XX = X_first_format  # ИСПОЛЬЗУЕМ ПОТОМ ЭТО!!!
