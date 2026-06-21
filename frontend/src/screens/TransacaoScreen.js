import React from 'react';
import { View, FlatList, Text } from 'react-native';
 
export default function TransacaoScreen() {
  const dados = [
    { id: '1', descricao: 'Salário', valor: 3000 },
    { id: '2', descricao: 'Mercado', valor: -200 }
  ];
 
  return (
    <View style={{ padding: 20 }}>
      <FlatList
        data={dados}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <Text>{item.descricao} - R$ {item.valor}</Text>
        )}
      />
    </View>
  );
}
 