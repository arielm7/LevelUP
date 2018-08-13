//
// Copyright (c) 2002-2018 WEINZIERL ENGINEERING GmbH
// All rights reserved.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
// SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DAMAGES OR OTHER LIABILITY,
// WHETHER IN CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
//

#include <kdrive/baos/Baos.h>
#include <kdrive/utility/Logger.h>
#include <Poco/Thread.h>
#include <Poco/Exception.h>
#include <Poco/Logger.h>
#include <Poco/ConsoleChannel.h>
#include <Poco/Format.h>

using namespace kdrive::baos;
using namespace kdrive::connector;
using Poco::Thread;
using Poco::Exception;
using Poco::format;

CLASS_LOGGER("LightSwitcher")

/*!
	Light Switcher

	This demo shows how to:

		create a connection with the BAOS device
		get/set Datapoint values
		read parameters

	It assumes an application with a single boolean bit (i.e. a light switch)
	which it turns on and off. A parameter is also used to specify the wait period
	before turning the light off.

	You will have to change the IP Address or device name to match your device.
	You can find the device name and ip address by running the Enumerator sample.
*/

/***********************************
** Anonymous namespace
************************************/

namespace
{

struct BaosApp
{
	enum CommunicationObjects { Ch1Request = 1 };
	enum Parameters { Ch1Timeout = 1 };
};

/*!
	sets the datapoint value to 1 or 0

	we read the value first to determine if it needs to be set.
	This is not normally required and you can simply set the value
	without reading it first. Implemented only to show how to
	read the datapoint value
*/


void waitTimeout(BaosConnector::Ptr connector)
{
	const int timeout = readParameter(connector, BaosApp::Ch1Timeout);

	poco_information(LOGGER(), format("Timeout is %d ms", timeout));

	Thread::sleep(2000);

}





void SetiarHora(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 2);

	datapoint.setTimeLocal();
	
	printf ("\n");
	printf ("se setio la hora con exito\n");
	printf ("\n");	
	
}



void PedirSegundo(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 2);

	int segundo = datapoint.getTimeSecond();
	printf ("\n");
	printf ("el segundo es %d", segundo);
	printf ("\n");
	
}


void PedirMinuto(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 2);

	int minuto = datapoint.getTimeMinute();
	printf ("\n");
	printf ("el minuto es %d", minuto);
	printf ("\n");
	
}


void PedirHora(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 2);

	int hora = datapoint.getTimeHour();
	printf ("\n");
	printf ("la hora es %d", hora);
	printf ("\n");
	
}

void PedirDia(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 2);

	int dia = datapoint.getTimeDay();

	printf ("\n");
	printf ("el dia es %d", dia);
	printf ("\n");
}






void obtenerConsumo(BaosConnector::Ptr connector, bool enabled)
{

	BaosDatapoint datapoint(connector, 4);

	int consumo = datapoint.get4OctetSigned();

	printf ("\n");
	printf ("el consumo es %d", consumo);
	printf ("\n");
	
}



void obtenerCoste(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector, 5);
	
	float coste = datapoint.get2OctetFloat();
	
	printf ("\n");	
	printf ("el coste es %f", coste);
	printf ("\n");


}







/*










void PrenderLuz(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector, 8);
	
	datapoint.setBoolean(true);
	
	printf ("\n");	
	printf ("luz encendida");
	printf ("\n");


}




void ApagarLuz(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector, 8);
	
	datapoint.setBoolean(false);
	
	printf ("\n");	
	printf ("luz apagada");
	printf ("\n");

}



void dimmmer_on(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector, 6);
	
	datapoint.setBoolean(true);
	
	printf ("\n");	
	printf ("dimmer on");
	printf ("\n");

}


void dimmmer_off(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector, 6);
	
	datapoint.setBoolean(false);
	
	printf ("\n");	
	printf ("dimmer off");
	printf ("\n");

}



void Brillo1(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,7);
	
	datapoint.setCharacterSet(20);
	
	printf ("\n");	
	printf ("luz al 15");
	printf ("\n");

}



void Brillo2(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,7);
	
	datapoint.setCharacterSet(100);	

	printf ("\n");	
	printf ("luz al 100");
	printf ("\n");

}



void Brillo3(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,7);
	
	datapoint.setCharacterSet(200);
	
	printf ("\n");	
	printf ("luz al 240");
	printf ("\n");

}



void Brillo11(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,11);
	
	datapoint.set3BitControl(true,2);	

	printf ("\n");	
	printf ("brillo al 20%");
	printf ("\n");

}




void Brillo22(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,11);
	
	datapoint.set3BitControl(true,4);	

	printf ("\n");	
	printf ("luz al 40%");
	printf ("\n");

}




void Brillo33(BaosConnector::Ptr connector, bool enabled)
{
	BaosDatapoint datapoint(connector,11);
	
	datapoint.set3BitControl(true,6);	

	printf ("\n");	
	printf ("luz al 60%");
	printf ("\n");

}




*/


} // end anonymous namespace

int main(int argc, char* argv[])
{
	try
	{
		// configure the logging channel
		INIT_ROOT_CONSOLE_LOGGER();

		// Find all available baos devices
		// and search for the "Baos-Sample" device
		BaosEnumerator baosEnumerator;
		const BaosEnumerator::Device device = baosEnumerator.findByAddress("192.168.10.100");

		// create a TPC/IP connection with the remote BAOS device
		// and attach to the connect and disconnect signals
		// set decodeProtocol to true to see the protocol information
		ScopedBaosConnection connection(device, true);
		BaosConnector::Ptr connector = connection.getConnector();
	

		SetiarHora(connector, true);
		waitTimeout(connector);
		PedirDia(connector, true);
		PedirHora(connector, true);
		PedirMinuto(connector, true);
		PedirSegundo(connector, true);
		obtenerConsumo(connector, true);
		obtenerCoste(connector, true);



		//Brillo1(connector, true);
		//Brillo11(connector, true);
/*		

		//PrenderLuz(connector, true);
		dimmmer_on(connector, true);
		

		waitTimeout(connector);
		Brillo1(connector, true);
		//Brillo11(connector, true);
		waitTimeout(connector);
		Brillo2(connector, true);
		//Brillo22(connector, true);
		waitTimeout(connector);		
		Brillo3(connector, true);
		//Brillo33(connector, true);


		waitTimeout(connector);


		//ApagarLuz(connector, true);
		dimmmer_off(connector, true);


*/











	}
	catch (Exception& exception)
	{
		LOGGER().log(exception);
	}

	return EXIT_SUCCESS;
}

