from js import console
import re
import random
#import hipervinculos as IP
import webbrowser




def hipervinculo(EVENTO):
    #RETICULAS---------------------------------------------------------------------------------
 if EVENTO == 'CALENDARIO':
    webbrowser.open_new(
        'https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Calendario%20Escolar%20Ciclo%202021-2022_Actualizado%20Enero%202022%20(1).pdf'
    )
 if EVENTO == 'SISTEMAS':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Sistemas%20Computacionales.pdf'
    )
 if EVENTO == 'INDUSTRIAL':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Industrial.pdf'
    )
 if EVENTO == 'ANIMACION':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Animaci%C3%B3n%20Digital%20y%20Efectos%20Visuales.pdf'
    )
 if EVENTO == 'ARQUITECTURA':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Arquitectura.pdf'
    )
 if EVENTO == 'CONTADURIA':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Contador%20P%C3%BAblico.pdf'
    )
 if EVENTO == 'LOGISTICA':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Logistica.pdf'
    )
 if EVENTO == 'QUIMICA':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Qu%C3%ADmica.pdf'
    )
 if EVENTO == 'ELECTRO':
     webbrowser.open_new(
    'http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Electromec%C3%A1nica.pdf'
    )
 if EVENTO == 'CONSTANCIA':
     webbrowser.open_new(
         'https://sfpya.edomexico.gob.mx/recaudacion/faces/municipios/organismosAuxiliares/OrganismosAuxiliares.xhtml#!'
     )
    
#c.open('https://docs.python.org/3/library/webbrowser.html')

def get_response(user_input):

    user_input = Element('user_input').element.value
    user_input_Element = Element('user_input') #innerHTML="<input id=\"user_input\"  type=\"text\" placeholder=\"Escribe aqui...\">"
    Element('test-output').element.innerHTML += "<br> <c style=\"justfy-self: end;\">"+ "TU: "+user_input + "</c>"
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    Element('test-output').element.innerHTML += "<br> <hr style=\"padding: 6px;\"> <br> <e>" +"TESJO: "+ response + "</e><hr style=\"padding: 6px;\">"
    #user_input_Element.innerHTML = '<script>var btn = document.getElementById(\'new-btn\');btn.addEventListener(\'click\', function(){document.getElementById(\'user_input\').value=\" \"})</script>'
    

    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}
        
        

        
        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)
            
        
    

        response('Hola bienvenido al asistente virtual del TESJO estoy a tus ordenes', ['hola', 'que tal', 'saludos', 'buenas'], single_response = True)
        response('Claro, ¿para que carrera?'+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Industrial.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería Industrial"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Animaci%C3%B3n%20Digital%20y%20Efectos%20Visuales.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería en Animación y Efectos Visuales"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Sistemas%20Computacionales.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería en Sistemas Computacionales"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Arquitectura.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Arquitectura"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Contador%20P%C3%BAblico.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Contador Público"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Licenciatura%20en%20Turismo.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Licenciatura en Turismo"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20en%20Logistica.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería en Logística"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Qu%C3%ADmica.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería Química"+ "</a>"+"<br>"+"<a href=\"http://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/reticulas/Reticulas2022/Ret%C3%ADcula%20Ingenier%C3%ADa%20Electromec%C3%A1nica.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Reticula de Ingeniería Electromecánica"+ "</a>"+"<br>", ['reticula', 'quiero una reticula'], required_words=['reticula'])
        response('Tel: (01712) 1231313 Correo: difusion@tesjo.edu.mx', ['contacto', 'correo', 'telefono', 'informes'], single_response=True)
        response('Muy bien aqui lo tienes ', ['calendario', 'calendario escolar', 'cal'],single_response=True) #required_words=['como'])
        response('Carretera Toluca-Atlacomulco KM 44.8 Ejido de San Juan y, San Agustin, 50700 Jocotitlán, Méx., México', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Para una constancia de estudios necesitas: '+"<br>"+' 1.- La ventana que se desplego llena tu formato de pago, recuerda seleccionar el Tecnologico de Estudios Superiores de Jocotitlan y llenar tus datos correctamente ademas de seleccionar el atributo de constancia de estudios.'+"<br>"+ '2.- Al haber concluido tu formulario descarga e imprime tu formato de pago y cubre el monto solicitado indicado en el mismo (en el formato de pago especifica los bancos donde puedes cubrir el pago).' +"<br>"+ '3.- Acude al TESJo en el edificio G en el departamente de control escolar y en un lapso de 1 a 2 dias tendras tu constancia.', ['como puedo sacar una constancia', 'constancia general', 'constancia'], single_response=True)
        response('Es un placer', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        #horarios
        response('Muy bien elige el horario de la carrera que estas buscando:'+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Arquitectura%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Horarios de Arquitectura"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Contador%20P%C3%BAblico%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Contador Publico"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20Electromec%C3%A1nica%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. Electromecanica"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20en%20Animaci%C3%B3n%20Digital%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. en Animación Digital y Efectos Visuales"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20en%20Gesti%C3%B3n%20Empresarial%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. en Gestión Empresarial"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20en%20Materiales%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. en Materiales"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20en%20Sistemas%20Computacionales%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. en Sistemas Computacionales"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20Industrial%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. Industrial"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20Mecatr%C3%B3nica%20Horarios%20Grupales%20F-A%202022(1).pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. Mecatrónica"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20Qu%C3%ADmica%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. Química"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Licenciatura%20en%20Turismo%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Licenciatura en Turismo"+ "</a>"+"<br>"+"<a href=\"https://tesjo.edomex.gob.mx/sites/tesjo.edomex.gob.mx/files/files/Ingenier%C3%ADa%20en%20Log%C3%ADstica%20Horarios%20Grupales%20F-A%202022.pdf\"style=\"color:#C5F7AF\"target=\"_blank\">Ing. en Logística"+ "</a>", ['horarios'],single_response=True)



        best_match = max(highest_prob, key=highest_prob.get)
    
        if best_match == 'Muy bien aqui lo tienes ':
            hipervinculo('CALENDARIO')
        if best_match ==  'Para una constancia de estudios necesitas: '+"<br>"+' 1.- La ventana que se desplego llena tu formato de pago, recuerda seleccionar el Tecnologico de Estudios Superiores de Jocotitlan y llenar tus datos correctamente ademas de seleccionar el atributo de constancia de estudios.'+"<br>"+ '2.- Al haber concluido tu formulario descarga e imprime tu formato de pago y cubre el monto solicitado indicado en el mismo (en el formato de pago especifica los bancos donde puedes cubrir el pago).' +"<br>"+ '3.- Acude al TESJo en el edificio G en el departamente de control escolar y en un lapso de 1 a 2 dias tendras tu constancia.':
            hipervinculo('CONSTANCIA')
 

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'lo siento no entendi eso','prueba contactar al TESJO'][random.randrange(4)]
    return response 