const User  = require('./User');
const UserRepository = require('./user-repository')

async function getUsers(){
  return UserRepository.findAll();
}

async function addUser(userData){
  const user = new User(userData);

  return UserRepository.addUser(user);
}

module.exports = {
  getUsers,
  addUser
}