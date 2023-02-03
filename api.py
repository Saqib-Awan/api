from flask import Flask,request,jsonify
import numpy as np
import pickle
model=pickle.load(open('Pickle File.pkl','rb'))

app=Flask(__name__)
@app.route('/predict',methods=['POST'])
def predict():
    Clump_Thickness=request.form.get('Clump_Thickness')
    Uniformity_of_Cell_Size=request.form.get('Uniformity_of_Cell_Size')
    Marginal_Adhesion=request.form.get('Marginal_Adhesion')
    Single_Epithelial_Cell_Size=request.form.get('Single_Epithelial_Cell_Size')
    Bare_Nuclei=request.form.get('Bare_Nuclei')
    Bland_Chromatin=request.form.get('Bland_Chromatin')

    input_query=np.array([[Clump_Thickness,Uniformity_of_Cell_Size,Marginal_Adhesion,
                           Single_Epithelial_Cell_Size,Bare_Nuclei,Bland_Chromatin,]])
    result=model.predict(input_query)[0]

    return jsonify({'tumor': str(result)})

if __name__ == '__main__':
    app.run(debug=True)