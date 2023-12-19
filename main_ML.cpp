//Tarea 1 Martin Valdivia y Luis Pérez
//Librerias necesarias para la ejecucion del programa
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cstdlib>

using namespace std;

//Creacion clase pregunta
class Pregunta{
private:
	string Enunciado;
	string Solucion;
	string Tiempo;
	string Taxonomia;
	string Tipopreg;
public:
	string tipo_pregunta;
	Pregunta(string Enunciado, string Solucion,string Tiempo, string Taxonomia,string Tipopreg);
	~Pregunta();
	string getEnunciado();
	string getSolucion();
	string getTiempo();
	string getTaxonomia();
	string getTipopreg();
};
//Constructor de la Clase Pregunta
Pregunta::Pregunta(string Enunciado, string Solucion, string Tiempo, string Taxonomia,string Tipopreg){
	this->Enunciado= Enunciado;
	this->Solucion= Solucion;
	this->Tiempo= Tiempo;
	this->Taxonomia= Taxonomia;
	this->Tipopreg=Tipopreg;
}
//Destructor de la Clase Pregunta
Pregunta::~Pregunta(){

}
//Getter para obtener la "info. privada" de la clase Pregunta
string Pregunta::getEnunciado(){
	return this->Enunciado;
}

string Pregunta::getSolucion(){
	return this->Solucion;
}

string Pregunta::getTiempo(){
	return this->Tiempo;
}

string Pregunta::getTaxonomia(){
	return this->Taxonomia;
}

string Pregunta::getTipopreg(){
	return this->Tipopreg;
}
//Creacion Clase Prueba
class Prueba{
private:
	int Ponderacion;
public:
	Prueba(int Ponderacion);
	~Prueba();
	int getPonderacion();
};
//Constructor
Prueba::Prueba(int Ponderacion){
	this->Ponderacion=Ponderacion;
}
//Destructor
Prueba::~Prueba(){
}
//Getter para la ponderacion de la Prueba
int Prueba::getPonderacion(){
	return this->Ponderacion;
}

int main(int argc, char** argv){
	//Variables para el funcionamiento del programa
	string opcion;
	int nro_preguntas, sumTiempo, Ponderacion;
	int preguntas_listas = 0;
	//Ingreso de la ponderacion de la prueba 
	cout << "Ingrese ponderacion" <<endl;
	cin>> Ponderacion;
	//Ingreso del nivel taxonomico deseado por el usuario 
	cout <<"Ingrese el nombre de la Taxonomia."<<endl;
	cout<<"Crear"<<endl;
	cout<<"Evaluar"<<endl;
	cout<<"Analizar"<<endl;
	cout<<"Aplicar"<<endl;
	cout<<"Entender"<<endl;
	cout<<"Recordar"<<endl;
	cout << "\n";
	cin >> opcion;
	//Ingreso de la cantidad de preguntas deseadas para la evaluacion
	cout <<"Ingrese la cantidad de preguntas:"<<endl;
	cin >> nro_preguntas;
	//LApertura del Archivo
	string nombreArchivo="datos.txt";
	ifstream archivo(nombreArchivo);
	string Enunciado, Solucion, Tiempo, linea, Taxonomia, Tipopreg;
	//Arreglo donde se guardaran las perguntas
	vector<Pregunta*> preguntas;
	//Lectura de archivo linea por linea y posterior ingreso al arreglo
	while(getline(archivo, linea)){
		istringstream iss(linea);
		getline(iss, Taxonomia, ',');
		getline(iss, Tipopreg, ',');
		getline(iss, Enunciado,',');
		getline(iss, Solucion, ',');
		getline(iss, Tiempo);
		Pregunta *nuevaPregunta = new Pregunta(Enunciado,Solucion,Tiempo,Taxonomia, Tipopreg);
		preguntas.push_back(nuevaPregunta);
	}
	//Bucle para ir revisando las preguntas obtenidas del archivo y comprobar cuales sirven para la prueba definida por el usuario
	for(int i=0; i<preguntas.size(); i++){
		//Si la cantidad de preguntas seleccionadas para la evaluacion es menor a la cantidad definida por el usuario  
		if(preguntas_listas<nro_preguntas){
			//Se comprueba que el nivel taxonomico ingresado corresponda al de la pregunta
			if(opcion == preguntas[i]->getTaxonomia()){
				//Y se obtiene la info de la pregunta
				cout << "Taxonomia " << i+1 << ": " << preguntas[i]->getTaxonomia()<< endl;
				cout << "Tipo de Pregunta " << i+1 << ": " << preguntas[i]->getTipopreg() << endl;
				cout << "Pregunta " << i+1 << ": " << preguntas[i]->getEnunciado() << endl;
				cout << "Solucion " << i+1 << ": " << preguntas[i]->getSolucion()<< endl;
				cout << "Tiempo " << i+1 << ": " << preguntas[i]->getTiempo()<< "\n";
				cout << "\n";
				sumTiempo += stoi(preguntas[i]->getTiempo());
				preguntas_listas++;
			}
		}
	}
	//Se presenta el tiempo total de la prueba 
	cout << "Tiempo total de prueba: " << sumTiempo << " Minutos" << endl;
	cout << "Fin de las prueba." << endl;
	return 0;
}
