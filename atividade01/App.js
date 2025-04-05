
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput, Button, TouchableOpacity } from 'react-native';

// Função para determinar o período do dia
const getPeriodOfDay = () => {
  const hour = new Date().getHours();
  if (hour < 12) return 'Bom dia';
  if (hour < 18) return 'Boa tarde';
  return 'Boa noite';
};

export default function App() {
  // Definir os estados para o nome do usuário e a saudação
  const [name, setName] = useState('');
  const [greeting, setGreeting] = useState('');

  // Função para atualizar a saudação
  const updateGreeting = () => {
    if (name.trim() !== '') {
      const period = getPeriodOfDay();
      setGreeting(`${period}, ${name}!`);
    }
  };

  // Função para limpar os campos
  const clearFields = () => {
    setName('');
    setGreeting('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Saudação Personalizada</Text>

      <TextInput
        style={styles.input}
        placeholder="Digite seu nome"
        value={name}
        onChangeText={setName}
      />

      <View style={styles.buttonContainer}>
        <Button title="Atualizar Saudação" onPress={updateGreeting} />
      </View>

      {greeting ? (
        <Text style={styles.greeting}>{greeting}</Text>
      ) : null}

      <TouchableOpacity onPress={clearFields}>
        <Text style={styles.clearButton}>Limpar</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f4f4f4',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    paddingLeft: 10,
    marginBottom: 20,
    width: '100%',
  },
  buttonContainer: {
    marginBottom: 20,
    width: '100%',
  },
  greeting: {
    fontSize: 18,
    color: '#4CAF50',
    fontWeight: 'bold',
  },
  clearButton: {
    fontSize: 16,
    color: '#FF6347',
    marginTop: 20,
    textDecorationLine: 'underline',
  },
});
