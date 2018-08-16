
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

	Thread::sleep(5000);

}


void obtenerConsumo(BaosConnector::Ptr connector)
{

	BaosDatapoint datapoint(connector, 2);

	int consumo = datapoint.get4OctetSigned();

	printf ("\n");
	printf ("el consumo es %d", consumo);
	printf ("\n");
	
}

void obtenerPotencia(BaosConnector::Ptr connector)
{

	BaosDatapoint datapoint(connector, 3);

	float consumo = datapoint.get2OctetFloat();

	printf ("\n");
	printf ("la potencia es %f", consumo);
	printf ("\n");
	
}




void PrenderLuz1(BaosConnector::Ptr connector)
{
	BaosDatapoint datapoint(connector, 1);
	
	datapoint.setBoolean(true);
	
	printf ("\n");	
	printf ("luz encendida");
	printf ("\n");
}
void ApagarLuz1(BaosConnector::Ptr connector)
{
	BaosDatapoint datapoint(connector, 1);
	
	datapoint.setBoolean(false);
	
	printf ("\n");	
	printf ("luz apagada");
	printf ("\n");
}



void PrenderLuz2(BaosConnector::Ptr connector)
{
	BaosDatapoint datapoint(connector, 4);
	
	datapoint.setBoolean(true);
	
	printf ("\n");	
	printf ("luz encendida");
	printf ("\n");
}
void ApagarLuz2(BaosConnector::Ptr connector)
{
	BaosDatapoint datapoint(connector, 4);
	
	datapoint.setBoolean(false);
	
	printf ("\n");	
	printf ("luz apagada");
	printf ("\n");
}



void Dimmer(BaosConnector::Ptr connector,int valor)
{
	BaosDatapoint datapoint(connector,5);
	
	datapoint.setCharacterSet(valor);	
	printf ("\n");
	printf ("dimmer al %d", valor);
	printf ("\n");
}



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
	

		
		obtenerConsumo(connector);
		obtenerPotencia(connector);
		PrenderLuz1(connector);
		waitTimeout(connector);
		ApagarLuz1(connector);
		waitTimeout(connector);
		PrenderLuz2(connector);
		waitTimeout(connector);
		Dimmer(connector,20);
		waitTimeout(connector);
		Dimmer(connector,100);
		waitTimeout(connector);
		Dimmer(connector,200);
		waitTimeout(connector);
		ApagarLuz2(connector);
		obtenerConsumo(connector);
		obtenerPotencia(connector);


	}
	catch (Exception& exception)
	{
		LOGGER().log(exception);
	}

	return EXIT_SUCCESS;
}
