import React from 'react';
import { View, Text, Button } from 'react-native';

export default function LoginScreen({ navigation }) {
  return (
    <View style={{ padding: 20 }}>
      <Text>Login</Text>
      <Button title="Entrar" onPress={() => navigation.navigate('Home')} />
    </View>
  );
}
