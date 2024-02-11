import { StyleSheet } from "react-native";

export const attractionTileStyles = StyleSheet.create({
    attractionTile: {
        
        backgroundColor: '#fff',
        padding: 20,
        marginVertical: 10,
        borderRadius: 10,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 3,
        elevation: 2,
        width: '100%',
    },
    attractionContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    filtersContainer:{
        alignItems: 'center',
        padding: 5,
        marginBottom: -20,
        marginTop: 5
    },
    leftContainer: {
        flexDirection: 'row',
        flex: 1,
        alignItems: 'center',
    },
    rightContainer: {
        flexDirection: 'column',
        alignItems: 'center',
    },
    imageContainer: {
        marginRight: 15,
    },
    image: {
        width: 70,
        height: 70,
        borderRadius: 15,
    },
    emptyImage: {
        width: 70,
        height: 70,
        borderRadius: 15,
        borderWidth: 1,
        borderColor: '#000',
        backgroundColor: 'transparent',
    },
    textContainer: {
        flexShrink: 1,
    },
    title: {
        fontWeight: 'bold',
        fontSize: 18,
        color: '#000',
    },
    category: {
        fontSize: 14,
        color: 'grey',
        marginBottom: 10,
    },
    reviews: {
        fontSize: 14,
        color: 'grey',
        marginVertical: 12,
    },
    description: {
        fontSize: 12,
        color: 'grey',
    },
    rate: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#FFD700',
    },
    sortFilterIndicator: {
        alignItems: 'center',
        fontFamily: 'Inter',
        fontSize: 20
    }
});
export const imagePlaceholder = StyleSheet.create({
    imageContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        marginTop: 20,
    },
    placeholder: {
        width: 450,
        height: 300,
        backgroundColor: '#abc',
        marginRight: 10,
    },
});
export const reviewModal = StyleSheet.create({
    backArrow: {
        fontFamily: 'Inter',
        fontSize: 48,
        padding: 5,
        marginTop: 10,
        color: '#0C0C0C',
        // fontWeight: 'bold',
    },
    modalContainer: {
        backgroundColor: 'white',
        // marginBottom: 600,
        height: '68%'
    },
    modalContent: {
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
        padding: 10,
        borderRadius: 10,
        marginBottom: 20,
    },
    filtersContainer: {
        backgroundColor: '#fff',
        justifyContent: 'space-between',
        flexDirection: 'row',
        padding: 10
    },
    buttonsContainer: {
        position: 'absolute',
        bottom: 10,
        left: 0,
        right: 0,
        flexDirection: 'row',
        justifyContent: 'flex-end',
        padding: 5,
        backgroundColor: '#fff',
    },
    addOpinionIcon: {
        width: 150,
        height: 44,
        backgroundColor: '#D5D2D2',
        borderRadius: 22,
        // marginLeft: -10,
        marginRight: 20,
        // marginTop: 2,
        marginBottom: 20,
        marginLeft: 10,
        shadowColor: '#000',
        shadowOffset: { width: 2, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 3,
        elevation: 2,
        alignItems: 'center',
    },
    addOpinionText: {
        fontSize: 28,
        color: '#0C0C0C',
        fontWeight: 'bold'
    },
});
export const reviewTile = StyleSheet.create({
    reviewTile: {
        backgroundColor: '#F8F8F8',
        padding: 5,
        marginVertical: 10,
        borderRadius: 10,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 3,
        elevation: 2,
    },
    image: {
        width: 50,
        height: 50,
        borderRadius: 15,
    },
    emptyImage: {
        width: 50,
        height: 50,
        borderRadius: 15,
        borderWidth: 1,
        borderColor: '#000',
        backgroundColor: 'transparent',
    },
    tileContainer: {
        padding: 5,
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        width: '100%',
    },
    title: {
        fontWeight: 'bold',
        marginHorizontal: 5,
        width: '70%',
        fontSize: 20,
        color: '#333',
    },
    description: {
        fontSize: 20,
        color: '#333',
    },
    author: {
        fontSize: 14,
        color: '#777',
        marginBottom: 10,
    },
    rate: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#FFA500',
    },
    price: {
        fontSize: 16,
        fontFamily: 'Inter',
        color: '#777',
        padding: 5,
        marginRight: 10,
        borderRadius: 15,
        borderWidth: 1,
        borderColor: '#000',
    },
    timeSpent: {
        fontSize: 16,
        fontFamily: 'Inter',
        color: '#777',
        padding: 5,
        marginLeft: 10,
        borderRadius: 15,
        borderWidth: 1,
        borderColor: '#000',
    },
    imageContainer: {
        flexDirection: 'row',
        justifyContent: 'flex-start',
        alignItems: 'center',
        padding: 5,
        marginTop: 10,
    },
    thumbnail: {
        width: 280,
        height: 200,
        marginRight: 10,
        borderRadius: 5,
    },
    imageModal: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
    },
    modalImage: {
        width: '80%',
        height: '80%',
        resizeMode: 'contain',
    },
    closeButton: {
        position: 'absolute',
        top: 20,
        right: 20,
    },
    closeText: {
        color: '#FFF',
        fontSize: 18,
    },
});