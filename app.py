import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import pickle
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prediction_house.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Intialize database


db = SQLAlchemy(app)




#Create db model

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
   
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

#Create a function to return string when we click the button

    def __repr__ (self):
        # return '<Name %r>' % self.id
        return 'friends'






model = pickle.load(open('my_model.pkl', 'rb'))

@app.route('/')

def home():
    return redirect('/other_features_of') 
    

@app.route('/other_features_of',methods=['POST' , 'GET'])


def other_features_of():

    

    if request.method == 'POST':
         if request.form.get('Gymnasium'):
            house_name = 'Gymnasium'
            house_list = Friends(name=house_name)
            

            # Push through database

            try:
                db.session.add(house_list)
                db.session.commit()
               
                
                return redirect('/other_features_of') 

            except:
                return "There was an error added the feature of the house"

         elif request.form.get('Swimming'):
            house_name = 'Swimming'
            house_list = Friends(name=house_name)

            # Push through database

            try:
                db.session.add(house_list)
                db.session.commit()

               
                return redirect('/other_features_of') 

            except:
                return "There was an error adding this feature of the house"

         elif request.form.get('Jogging_track'):
            house_name = 'Jogging track'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Indoor_Games'):
            house_name = 'Indoor Games'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Club_house'):
            house_name = 'Club house'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Cafeteria'):
            house_name = 'Cafeteria'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Golf_course'):
            house_name = 'Golf course'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Lift'):
            house_name = 'Lift'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Power_backup'):
            house_name = 'Power backup'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Car_Parking'):
            house_name = 'Car Parking'
            house_list = Friends(name=house_name)
            db.session.add(house_list)
            db.session.commit()    
            return redirect('/other_features_of')

         elif request.form.get('Submit'):  
            return redirect('/submit')
    
    else:    
     
       friends = Friends.query.order_by(Friends.date_created)
        

       return render_template('extend.html', friends = friends )

             
    return render_template('extend.html')  


    


@app.route('/submit' , methods=['POST' , 'GET'])

def extension():
    my_list_features = []
    my_list = []
    my_house = []
    
    friends = Friends.query.order_by(Friends.date_created)
    for friend in friends:
        my_list_features.append(friend.name)


    for m in range(44):
        my_list.append(1)

    my_list[4] = 0

    my_list[5] = 0

    my_list[7] = 0 

    my_list[9] = 0

    my_list[17] = 0

    my_list[18] = 0

    my_list[20] = 0

    my_list[28] = 0

    my_list[32] = 0


    for n in my_list_features:
        if n =='Gymnasium' and n in my_list_features:
            my_list[4] = 1
                
        elif n == 'Swimming'and n in my_list_features:
            my_list[5] = 1

        elif n == 'Jogging track' and n in my_list_features:
            my_list[7] = 1

        elif n == 'Indoor Games' and n in my_list_features:
            my_list[9] = 1

        elif n == 'Power backup' and n in my_list_features:
            my_list[17] = 1

        elif n == 'Car Parking' and n in my_list_features:
            my_list[18] = 1

        elif n == 'Cafeteria' and n in my_list_features:
            my_list[20] = 1
            
        elif n == 'Lift' and n in my_list_features:
            my_list[28] = 1

        elif n == 'Golf course' and n in my_list_features:
            my_list3[2] = 1

    if request.method =='POST':
        if request.form.get('Predict'):
            try:
                a = request.form['bed_rooms']      
                my_list[0] = int(a)
                final_features = [np.array(my_list)]
                prediction = model.predict(final_features)
                output = round(prediction[0], 2) 
                return render_template('extend.html', friends = friends ,mylist = 'This is my list {}'.format(my_list), output ='Price of the house is $ {}'.format(output))

            except:

                return 'Please enter the correct value in the place of "No of bedrooms"'



    

    

    

    

    

    return render_template('extend.html', friends = friends ,mylist = 'This is my list {}'.format(my_list))




    

    
@app.route('/delete/<int:student_id>', methods = ['POST' , 'GET'])
def delete(student_id):
    #friends = Friends.query.order_by(Friends.date_created)
    delete_features2 = Friends.query.all()
    try:
        value_Delete = Friends.query.get_or_404(student_id)
        db.session.delete(value_Delete)
        db.session.commit()
        return redirect('/other_features_of')

    except:

        return "There was a problem deleting and the delete_features are {} " .format(Friends.query.all())   
   


@app.route('/values' , methods = ['POST' , 'GET'])

def values():

    a = Friends.query.get_or_404(2)
    db.session.delete(a)
    db.session.commit()

    return 'The querys are :{}'.format(a)      



    

if __name__ == "__main__":
    app.run(debug=True)