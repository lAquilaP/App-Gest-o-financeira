import React from 'react';
import { View, Text, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={{ padding: 20 }}>
      <Text>Dashboard</Text>
      <Text>Saldo: R$ 2000</Text>

      <Button title="Ver Transações" onPress={() => navigation.navigate('Transacoes')} />
    </View>
  );
}
