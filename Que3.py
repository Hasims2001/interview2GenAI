from flask import Flask, request, jsonify
import json
app = Flask(__name__)


posts = []

@app.route('/post', methods=['POST', "GET"])
def postPosts():
    global posts
    if(request.method == 'POST'):
        try:
            res = request.get_json()
            data = json.dumps(res)
        
            posts.append(data)
            return jsonify({'message': "post added!"})

        except:
            return jsonify({'message': "something is wrong"})

    return jsonify({'message': "All posts", 'posts': posts})


@app.route('/post/<int:id>', methods=['DELETE'])
def deletePosts(id):
    global posts
    try:
        ind = 0
        flag = False
        for each in posts:
            if(each['id'] == id):
                flag = True
                break
            ind += 1    
        
        if(flag):
            posts.pop(ind)
        else:
            return jsonify({'message': f"post with id {id} is not present"})
    except:
        return jsonify({'message': "something is wrong"})
    
    
if(__name__ == '__main__'):
    app.run(debug=True)