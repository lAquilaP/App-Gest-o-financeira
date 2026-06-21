import { View, Text, Pressable, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
 
export default function HomeScreen() {
  const router = useRouter();
 
  return (
    <View style={styles.container}>
      <Text style={styles.titulo}>Dashboard</Text>
 
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Saldo Atual</Text>
        <Text style={styles.saldo}>R$ 2.000</Text>
      </View>
 
      <Pressable style={styles.botao} onPress={() => router.push('/transacoes')}>
        <Text style={styles.botaoTexto}>Ver Transações</Text>
      </Pressable>
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
    fontWeight: 'bold',
    marginBottom: 30,
  },
  card: {
    backgroundColor: '#1E1E1E',
    borderRadius: 15,
    padding: 25,
    marginBottom: 30,
    elevation: 5,
  },
  cardTitle: {
    color: '#aaa',
    marginBottom: 10,
  },
  saldo: {
    color: '#00C853',
    fontSize: 28,
    fontWeight: 'bold',
  },
  botao: {
    backgroundColor: '#00C853',
    padding: 15,
    borderRadius: 12,
  },
  botaoTexto: {
    color: '#fff',
    textAlign: 'center',
    fontWeight: 'bold',
  },
});
 