def global_nav(request):
    return  {
   'nav' : [
            [ 'index' , 'Home'],
            [ 'blog:index' , 'My Blog 📝'],
            [ 'project:index' , 'My Project 🚀'],
            [ 'about:index' , 'About Me 😊'],
            [ 'contact:index' , 'Contact Me 💌'],

        ]
}

def bg_global (request):
    return {
        'img' : [
            ['img/dolp.png' , 'dolp'],
            ['img/dolp1.jpg' , 'dolp1'],
            ['img/dolp2.jpg' , 'dolp2'],
            ['img/dolp3.jpg' , 'dolp3'],
            ['img/dolp4.jpg' , 'dolp4'],
        ]
    }