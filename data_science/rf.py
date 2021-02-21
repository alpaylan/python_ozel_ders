import pandas as pd

df = pd.read_csv('archive/heart.csv')
df_data = df.drop(columns=['target'])
df_target = df.get('target')


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df_data, df_target, test_size=0.33, random_state=42)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=20)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(pred, y_test))

from sklearn.tree import export_graphviz

export_graphviz(clf.estimators_[0],
                out_file='tree.dot',
                rounded = True, proportion = False,
                precision = 2, filled = True)

from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

