import { View, Text, FlatList, StyleSheet } from 'react-native';
 
export default function TransacaoScreen() {
  const dados = [
    { id: '1', descricao: 'Salário', valor: 3000 },
    { id: '2', descricao: 'Mercado', valor: -200 },
  ];
 
  return (
    <View style={styles.container}>
      <Text style={styles.titulo}>Transações</Text>
 
      <FlatList
        data={dados}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.desc}>{item.descricao}</Text>
 
            <Text
              style={[
                styles.valor,
                { color: item.valor > 0 ? '#00C853' : '#FF3D00' },
              ]}
            >
              R$ {item.valor}
            </Text>
          </View>
        )}
      />
    </View>
  );
}
 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0D0D0D',
    padding: 20,
  },
  titulo: {
    color: '#fff',
    fontSize: 24,
    marginBottom: 20,
    fontWeight: 'bold',
  },
  card: {
    backgroundColor: '#1E1E1E',
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  desc: {
    color: '#fff',
  },
  valor: {
    fontWeight: 'bold',
  },
});
 