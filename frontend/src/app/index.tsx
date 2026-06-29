import { View, Text, Pressable, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
 
export default function LoginScreen() {
  const router = useRouter();
 
  return (
    <View style={styles.container}>
      <Text style={styles.logo}>💰 Controle Financeiro</Text>
 
      <Pressable style={styles.botao} onPress={() => router.push('/home')}>
        <Text style={styles.botaoTexto}>Entrar</Text>
      </Pressable>
    </View>
  );
}
 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0D0D0D',
    justifyContent: 'center',
    alignItems: 'center',
  },
  logo: {
    fontSize: 26,
    color: '#fff',
    marginBottom: 50,
    fontWeight: 'bold',
  },
  botao: {
    backgroundColor: '#00C853',
    paddingVertical: 15,
    paddingHorizontal: 40,
    borderRadius: 12,
    elevation: 5,
  },
  botaoTexto: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
 