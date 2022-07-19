
import sys

clients = [
  {
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer'
  },
  {
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data engineer'
  }
  ]

def createClient(client):
  global clients

  if client not in clients:
    clients.append(client)
  else:
    print('Sorry, this client already exists') 


def searchClient(clientName):
  for client in clients:
    if client != clientName:
      continue
    else:
      return True


def updateClient(clientName, updatedClientName):
  global clients

  if clientName in clients:
    index = clients.index(clientName)
    clients[index] = updatedClientName
    listClients()
  else:
    print('Sorry the name of the client not exists')


def deleteClient(clientName):
  global clients

  if clientName in clients:
    clients.remove(clientName)
    listClients()
  else:
    print('Sorry the name of the client not exists')


def listClients():
  for idx, client in enumerate(clients):    
    print('{idx} | {name} | {company} | {email} | {position}'.format(
      idx=idx,
      name=client['name'],
      company=client['company'],
      email=client['email'],
      position=client['position']
    ))

def _getClientField(field_name):
  field = None

  while not field:
    field = input('what is the client {}? '.format(field_name))
  
  return field


def _getClientName():
  clientName = None
  while not clientName:
    clientName = input('What is the client name: ')
    if clientName == 'exit':
      clientName = None
      break
  if not clientName:
    sys.exit()

  return clientName


def printWelcome():
  print('¡Welcome to Platzi-ventas!')
  print('*' * 50)
  print('What would you do today?')
  print('[L]ist clients')
  print('[C]reate client')
  print('[S]earch client')
  print('[U]pdate client')
  print('[D]elete client')  


if __name__ == '__main__':
  printWelcome()

  command = input()
  command = command.upper()

  if command == 'C':
    client = {
      'name': _getClientField('name'),
      'company': _getClientField('company'),
      'email': _getClientField('email'),
      'position': _getClientField('position')
    }
    createClient(client)
    listClients()

  elif command == 'L':
    listClients()
  elif command == 'D' :
    listClients()
    clientName = input('What is the name of the client to delete: ')
    deleteClient(clientName)
  elif command == 'S':
    clientName = _getClientName()
    found = searchClient(clientName)
    if found:
      print('The client was found in the list')
    else:
      print('Error, the client: {} doesnt exists in our clients list'.format(clientName))
  elif command == 'U' :
    listClients()
    clientName = _getClientName() 
    updatedClientName = input('What is the name to update de client: ')
    updateClient(clientName, updatedClientName)
  else:
    print('Sorry invalid command')
    sys.exit()