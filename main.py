from aiogram import Dispatcher, Bot, filters, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

bot = Bot(token="7487391209:AAHwnZ3XZfQCdSIo1OrgdOup_HCGyy6Nx7Q")
dp = Dispatcher(bot=bot)

orders = []


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()
    first_name2 = State()
    last_name2 = State()
    number2 = State()
    card = State()
    card2 = State()


main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="O'zbek tili"), KeyboardButton(text="Русский язык")]
], resize_keyboard=True)


contact_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)


contact_button_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Отправить контакт", request_contact=True)]
], resize_keyboard=True)

menu_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Еда"), KeyboardButton(text="Напитки")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True)

menus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Ovqat"), KeyboardButton(text="Ichimlik")],
    [KeyboardButton(text="Orqaga")]
], resize_keyboard=True)

food = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Lavash"), KeyboardButton(text="Burger"), KeyboardButton(text="Hot-Dog")],
    [KeyboardButton(text="Fri"), KeyboardButton(text="Shaurma"), KeyboardButton(text="Chizburger")]
], resize_keyboard=True)


food_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Лаваш"), KeyboardButton(text="Бургер"), KeyboardButton(text="Хот-Дог")],
    [KeyboardButton(text="Картошка Фри"), KeyboardButton(text="Шаурма"), KeyboardButton(text="Чизбургер")]
], resize_keyboard=True)

drink = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Cola"), KeyboardButton(text="Fanta"), KeyboardButton(text="Pepsi")],
    [KeyboardButton(text="Asu"), KeyboardButton(text="Lipton"), KeyboardButton(text="Suv")]
], resize_keyboard=True)


drink_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кола"), KeyboardButton(text="Фанта"), KeyboardButton(text="Пепси")],
    [KeyboardButton(text="Асу"), KeyboardButton(text="Липтон"), KeyboardButton(text="Вода")]
], resize_keyboard=True)


baskets = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Hammasini sotib olish"), KeyboardButton(text="Hammasini o'chirish")],
    [KeyboardButton(text="Orqaga")]
], resize_keyboard=True)

baskets_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Купить все товары"), KeyboardButton(text="Удалить все товары")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True)




reception = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Menu")],
    [KeyboardButton(text="Savat")],
    [KeyboardButton(text="Biz haqimizda")],
    [KeyboardButton(text="Sizning ma'lumotingiz")],
    [KeyboardButton(text="qo'llab-quvvatlash xizmati")],
    [KeyboardButton(text="Tilni o'zgartirish")]
], resize_keyboard=True)


reception_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="О нас")],
    [KeyboardButton(text="Ваша информация")],
    [KeyboardButton(text="Служба поддержки")],
    [KeyboardButton(text="Поменять язык")]
], resize_keyboard=True)


@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer("Tilni ta'nlang", reply_markup=main_button)


@dp.message(F.text == "Русский язык")
async def rus_lang(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name2)
    await message.answer("Имя: ")


@dp.message(Registration.first_name2)
async def first_name_rus(message: types.Message, state: FSMContext):
    await state.update_data(first_name2=message.text)
    await state.set_state(Registration.last_name2)
    await message.answer("Фамилия: ")


@dp.message(Registration.last_name2)
async def last_name_rus(message: types.Message, state: FSMContext):
    await state.update_data(last_name2=message.text)
    await state.set_state(Registration.number2)
    await message.answer("Номер: ", reply_markup=contact_button_rus)


@dp.message(Registration.number2)
async def phone2_number(message: types.Message, state: FSMContext):
    await state.update_data(number2=message.contact.phone_number)
    user_data = await state.get_data()
    await message.answer(f"Имя: {user_data['first_name2']}\n"
                         f"Фамилия: {user_data['last_name2']}\n"
                         f"Номер: {user_data['number2']}", reply_markup=reception_rus)
    await state.clear()



@dp.message(F.text == "O'zbek tili")
async def register(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Ism: ")


@dp.message(Registration.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Familya: ")


@dp.message(Registration.last_name)
async def last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Nomer: ", reply_markup=contact_button)


@dp.message(Registration.number)
async def phone_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    user_data = await state.get_data()
    await message.answer(f"Sizning ismingiz: {user_data['first_name']}\n"
                         f"Sizning familiyangiz: {user_data['last_name']}\n"
                         f"Sizning nomeringiz: {user_data['number']}", reply_markup=reception)
    await state.clear()


@dp.message(F.text == "Menu")
async def menu(message: types.Message):
    await message.answer("Ovqat yoki ichimlik?", reply_markup=menus)


@dp.message(F.text == "Меню")
async def menu2(message: types.Message):
    await message.answer("Еда или Напитки?", reply_markup=menu_rus)


@dp.message(F.text == "Ovqat")
async def food_function(message: types.Message):
    await message.answer("Siz ovqat bo'limini tanladingiz", reply_markup=food)


@dp.message(F.text == "Еда")
async def food2_function(message: types.Message):
    await message.answer("Вы выбрали раздел еды", reply_markup=food_rus)


@dp.message(F.text == "Ichimlik")
async def drink_function(message: types.Message):
    await message.answer("Siz ichimlik bo'limini tanladingiz", reply_markup=drink)


@dp.message(F.text == "Напитки")
async def drink2_function(message: types.Message):
    await message.answer("Вы выбрали раздел напиток", reply_markup=drink_rus)


@dp.message(F.text == "Orqaga")
async def back_function(message: types.Message):
    await message.answer("Siz ortga qayttiz", reply_markup=reception)


@dp.message(F.text == "Назад")
async def back2_function(message: types.Message):
    await message.answer("ВЫ вернулись назад", reply_markup=reception_rus)


@dp.message(F.text == "Biz haqimizda")
async def about_us(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/800px-Apple_logo_black.svg.png",
                               caption="Apple Inc. – shtab-kvartirasi Kupertinoda (Kaliforniya) joylashgan Amerika koʻp millatli texnologiya kompaniyasi. Apple 2022-yilda 394,3 milliard dollar daromad "
                         "bilan dunyoning eng yirik texnologiya kompaniyasi "
                         "hisoblanadi. 2023 yil mart holatiga koʻra, "
                         "Apple bozor kapitallashuvi boʻyicha dunyodagi "
                         "eng yirik kompaniya hisoblanadi. 2022 yil "
                         "iyun holatiga koʻra, Apple shaxsiy kompyuterlar "
                         "sotuvchisi boʻyicha toʻrtinchi va dunyodagi ikkinchi yirik mobil "
                         "telefon ishlab chiqaruvchisi. U Alphabet (Google kompaniyasining bosh kompaniyasi), Amazon,"
                         " Meta Platforms va Microsoft bilan bir qatorda Amerikaning Katta beshlik axborot texnologiyalari kompaniyalaridan"
                         " biri hisoblanadi.", reply_markup=reception)


@dp.message(F.text == "О нас")
async def about2_us(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/800px-Apple_logo_black.svg.png",
                               caption="Apple — американская корпорация, разработчик"
                                       " персональных и планшетных компьютеров, "
                                       "аудиоплееров, смартфонов, программного "
                                       "обеспечения и цифрового контента. "
                                       "Штаб-квартира расположена в Купертино, "
                                       "штат Калифорния.", reply_markup=reception_rus)



@dp.message(F.text == "Sizning ma'lumotingiz")
async def user_info(message: types.message):
    await message.answer(f"Username: {message.from_user.username}\nFull name: {message.from_user.full_name}\n"
                         f"Id: {message.from_user.id}", reply_markup=reception)


@dp.message(F.text == "Ваша информация")
async def user2_info(message: types.message):
    await message.answer(f"Username: {message.from_user.username}\nFull name: {message.from_user.full_name}\n"
                         f"Id: {message.from_user.id}", reply_markup=reception_rus)


@dp.message(F.text == "qo'llab-quvvatlash xizmati")
async def support(message: types.Message):
    await message.answer("Qo'llab-quvvatlash xizmati: +998-(33)-530-72-27", reply_markup=reception)


@dp.message(F.text == "Служба поддержки")
async def support2(message: types.Message):
    await message.answer("Служба поддержки: +998-(33)-530-72-27", reply_markup=reception_rus)



@dp.message(F.text == "Savat")
async def show_basket(message: types.Message):
    global orders
    if orders:
        basket_content = "\n".join(orders)
        await message.answer(f"Sizning savatingiz:\n{basket_content}", reply_markup=baskets)
    else:
        await message.answer("Savatingiz bo'sh", reply_markup=reception)


@dp.message(F.text == "Корзина")
async def show2_basket(message: types.Message):
    global orders
    if orders:
        basket_content = "\n".join(orders)
        await message.answer(f"Ваша корзина:\n{basket_content}", reply_markup=baskets_rus)
    else:
        await message.answer("Корзина пустая", reply_markup=reception_rus)


@dp.message(F.text == "Hammasini o'chirish")
async def clear_basket(message: types.Message):
    global orders
    orders = []
    await message.answer("Savat muvaffaqiyatli bo'shatildi", reply_markup=reception)


@dp.message(F.text == "Удалить все товары")
async def clear2_basket(message: types.Message):
    global orders
    orders = []
    await message.answer("Корзинка успешно очищена", reply_markup=reception_rus)


cards = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Humo"), KeyboardButton(text="Uzcard")]
], resize_keyboard=True)


cards_rus = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Хумо"), KeyboardButton(text="Узкард")]
], resize_keyboard=True)


@dp.message(F.text == "Hammasini sotib olish")
async def buy_all_basket(message: types.Message):
    await message.answer("Qaysi karta bilan to'lo'vni amal qilmoqchisiz", reply_markup=cards)


@dp.message(F.text == "Купить все товары")
async def buy2_all_basket(message: types.Message):
    await message.answer("С какой картой хотите оплатить", reply_markup=cards_rus)



@dp.message(F.text == "Humo")
async def humo_card(message: types.Message, state: FSMContext):
    await state.set_state(Registration.card)
    await message.answer("Kartani nomerini kiriting", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Хумо")
async def humo2_card(message: types.Message, state: FSMContext):
    await state.set_state(Registration.card2)
    await message.answer("Введите номер карты", reply_markup=ReplyKeyboardRemove())


@dp.message(Registration.card)
async def card_process(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    int(card_number)
    if card_number.isdigit() and len(card_number) >= 16:
        await message.answer("Hammasi sotib olindi", reply_markup=reception)
        global orders
        orders.clear()
        await state.clear()
    else:
        await message.answer("Noto'g'ri kartani nomerini kiritdingiz. Iltimos, 16 raqamdan ko'p bo'lgan to'g'ri kartani kiriting.")


@dp.message(Registration.card2)
async def card2_process(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    int(card_number)
    if card_number.isdigit() and len(card_number) >= 16:
        await message.answer("Все товары выкуплены", reply_markup=reception_rus)
        global orders
        orders.clear()
        await state.clear()
    else:
        await message.answer("Вы ввели неправильный номер карты. Пожалуйста, введите действительную карту, содержащую более 16 цифр.")


@dp.message(F.text == "Uzcard")
async def uzcard(message: types.Message, state: FSMContext):
    await state.set_state(Registration.card)
    await message.answer("Kartani nomerini kiriting", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Узкард")
async def uzcard2(message: types.Message, state: FSMContext):
    await state.set_state(Registration.card2)
    await message.answer("Введите номер карты", reply_markup=ReplyKeyboardRemove())


@dp.message(Registration.card)
async def uzcard_process(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    int(card_number)

    if card_number.isdigit() and len(card_number) >= 16:
        await message.answer("Hammasi sotib olindi", reply_markup=reception)
        global orders
        orders.clear()
        await state.clear()
    else:
        await message.answer("Noto'g'ri kartani nomerini kiritdingiz. Iltimos, 16 raqamdan ko'p bo'lgan to'g'ri kartani kiriting.")


@dp.message(Registration.card2)
async def uzcard2_process(message: types.Message, state: FSMContext):
    card_number = message.text.strip()
    int(card_number)

    if card_number.isdigit() and len(card_number) >= 16:
        await message.answer("Все товары выкуплены", reply_markup=reception_rus)
        global orders
        orders.clear()
        await state.clear()
    else:
        await message.answer(
            "Вы ввели неправильный номер карты. Пожалуйста, введите действительную карту, содержащую более 16 цифр."
        )


suv_multiple = [
    [InlineKeyboardButton(text="Suv sotib olish", callback_data="suv-olish"), InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]
]

multipleChoice = InlineKeyboardMarkup(inline_keyboard=suv_multiple)


@dp.message(F.text == "Suv")
async def water(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXTi2k3KZmuzWTOpnIzOW6q3EcInt3uzUx-Q&s",
                               caption="Suv : $1",
                               reply_markup=multipleChoice)


@dp.callback_query(F.data == "suv-olish")
async def buy_product(callback: types.CallbackQuery):
    global orders
    orders.append("Suv\n")
    await callback.message.answer("Suv savatga qo'shildi", reply_markup=reception)


suv_multiple_rus = [
    [InlineKeyboardButton(text="Купить воду", callback_data="вода"), InlineKeyboardButton(text="Отменить", callback_data="отмена")]
]

multipleChoice_rus = InlineKeyboardMarkup(inline_keyboard=suv_multiple_rus)


@dp.message(F.text == "Вода")
async def water2(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXTi2k3KZmuzWTOpnIzOW6q3EcInt3uzUx-Q&s",
                               caption="Вода : $1",
                               reply_markup=multipleChoice_rus)


@dp.callback_query(F.data == "вода")
async def buy2_product(callback: types.CallbackQuery):
    global orders
    orders.append("Вода\n")
    await callback.message.answer("Вода добавлена в корзину", reply_markup=reception_rus)


cola_multiple = [
    [InlineKeyboardButton(text="Cola sotib olish", callback_data="cola-olish"), InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]
]

multipleChoice2 = InlineKeyboardMarkup(inline_keyboard=cola_multiple)


@dp.message(F.text == "Cola")
async def cola(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Glass_of_Cola.jpg/800px-Glass_of_Cola.jpg",
                               caption="Cola : $2",
                               reply_markup=multipleChoice2)


@dp.callback_query(F.data == "cola-olish")
async def buy_cola(callback: types.CallbackQuery):
    global orders
    orders.append("Cola\n")
    await callback.message.answer("Cola savatga qo'shildi", reply_markup=reception)



cola_multiple_rus = [
    [InlineKeyboardButton(text="Купить колу", callback_data="кола"), InlineKeyboardButton(text="Отменить", callback_data="отмена")]
]

multipleChoice2_rus = InlineKeyboardMarkup(inline_keyboard=cola_multiple_rus)


@dp.message(F.text == "Кола")
async def cola2(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Glass_of_Cola.jpg/800px-Glass_of_Cola.jpg",
                               caption="Кола : $2",
                               reply_markup=multipleChoice2_rus)


@dp.callback_query(F.data == "кола")
async def buy2_cola(callback: types.CallbackQuery):
    global orders
    orders.append("Кола\n")
    await callback.message.answer("Кола добавлена в корзину", reply_markup=reception_rus)


multipleChoice3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Pepsi sotib olish", callback_data="pepsi-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


@dp.message(F.text == "Pepsi")
async def pepsi(message: types.Message):
    await message.answer_photo(photo="https://t4.ftcdn.net/jpg/02/84/65/61/360_F_284656175_G6SlGTBVl4pg8oXh6jr86cOmKUZjfrym.jpg",
                               caption="Pepsi : $1",
                               reply_markup=multipleChoice3)


@dp.callback_query(F.data == "pepsi-olish")
async def buy_pepsi(callback: types.CallbackQuery):
    global orders
    orders.append("Pepsi\n")
    await callback.message.answer("Pepsi savatga qo'shildi", reply_markup=reception)


pepsi_multiple_rus = [
    [InlineKeyboardButton(text="Купить пепси", callback_data="пепси"), InlineKeyboardButton(text="Отменить", callback_data="отмена")]
]

multipleChoice3_rus = InlineKeyboardMarkup(inline_keyboard=pepsi_multiple_rus)


@dp.message(F.text == "Пепси")
async def pepsi2(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Glass_of_Cola.jpg/800px-Glass_of_Cola.jpg",
                               caption="Пепси : $2",
                               reply_markup=multipleChoice3_rus)


@dp.callback_query(F.data == "пепси")
async def buy2_pepsi(callback: types.CallbackQuery):
    global orders
    orders.append("Пепси\n")
    await callback.message.answer("Пепси добавлена в корзину", reply_markup=reception_rus)


multipleChoice4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Asu sotib olish", callback_data="asu-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


@dp.message(F.text == "Asu")
async def asu(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_QmAUvyXBJnx4cwctJCtsOXFQ-O8TWrkNyg&s",
                               caption="Asu : $0.7",
                               reply_markup=multipleChoice4)


@dp.callback_query(F.data == "asu-olish")
async def buy_asu(callback: types.CallbackQuery):
    global orders
    orders.append("Asu\n")
    await callback.message.answer("Asu savatga qo'shildi", reply_markup=reception)


multipleChoice4_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить асу", callback_data="асу"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Асу")
async def asu2(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_QmAUvyXBJnx4cwctJCtsOXFQ-O8TWrkNyg&s",
                               caption="Асу : $0.7",
                               reply_markup=multipleChoice4_rus)


@dp.callback_query(F.data == "асу")
async def buy2_asu(callback: types.CallbackQuery):
    global orders
    orders.append("Асу\n")
    await callback.message.answer("Асу добавлена в корзину", reply_markup=reception_rus)


multipleChoice5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Lipton sotib olish", callback_data="lipton-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


@dp.message(F.text == "Lipton")
async def lipton(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdm0RZpi4WsrgcOTOQBqphiQNG6LH9JPjEkA&s",
                               caption="Lipton : $1.2",
                               reply_markup=multipleChoice5)


@dp.callback_query(F.data == "lipton-olish")
async def buy_lipton(callback: types.CallbackQuery):
    global orders
    orders.append("Lipton\n")
    await callback.message.answer("Lipton savatga qo'shildi", reply_markup=reception)


multipleChoice5_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить липтон", callback_data="липтон"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Липтон")
async def lipton2(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdm0RZpi4WsrgcOTOQBqphiQNG6LH9JPjEkA&s",
                               caption="Липтон : $1.2",
                               reply_markup=multipleChoice5_rus)


@dp.callback_query(F.data == "липтон")
async def buy2_lipton(callback: types.CallbackQuery):
    global orders
    orders.append("Липтон\n")
    await callback.message.answer("Липтон добавлено в корзину", reply_markup=reception_rus)


multipleChoice6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Fanta sotib olish", callback_data="fanta-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


multipleChoice6_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить фанту", callback_data="фанта"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Fanta")
async def fanta(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNf9tWMwn28xTWM3Gjs7TgxdL6iaAK4WcLQg&s",
                               caption="Fanta : $1.5",
                               reply_markup=multipleChoice6)


@dp.message(F.text == "Фанта")
async def fanta2(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNf9tWMwn28xTWM3Gjs7TgxdL6iaAK4WcLQg&s",
                               caption="Фанта : $1.5",
                               reply_markup=multipleChoice6_rus)


@dp.callback_query(F.data == "fanta-olish")
async def buy_fanta(callback: types.CallbackQuery):
    global orders
    orders.append("Fanta\n")
    await callback.message.answer("Fanta savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "фанта")
async def buy2_fanta(callback: types.CallbackQuery):
    global orders
    orders.append("Фанта\n")
    await callback.message.answer("Фанта добавлена в корзину", reply_markup=reception_rus)


foodChoice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Lavash sotib olish", callback_data="lavash-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


foodChoice_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить лаваш", callback_data="лаваш"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Lavash")
async def lavash(message: types.Message):
    await message.answer_photo(photo="https://media.express24.uz/r/:w/:h/USkw4zygayqAjhGTgd5qZ.jpg",
                               caption="lavash : $2",
                               reply_markup=foodChoice)


@dp.message(F.text == "Лаваш")
async def lavash2(message: types.Message):
    await message.answer_photo(photo="https://media.express24.uz/r/:w/:h/USkw4zygayqAjhGTgd5qZ.jpg",
                               caption="Лаваш : $2",
                               reply_markup=foodChoice_rus)


@dp.callback_query(F.data == "lavash-olish")
async def buy_lavash(callback: types.CallbackQuery):
    global orders
    orders.append("Lavash\n")
    await callback.message.answer("Lavash savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "лаваш")
async def buy2_lavash(callback: types.CallbackQuery):
    global orders
    orders.append("Лаваш\n")
    await callback.message.answer("Лаваш добавлен в корзину", reply_markup=reception_rus)



foodChoice2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Burger sotib olish", callback_data="burger-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])


foodChoice2_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить бургер", callback_data="бургер"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Burger")
async def burger(message: types.Message):
    await message.answer_photo(photo="https://www.foodandwine.com/thmb/DI29Houjc_ccAtFKly0BbVsusHc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/crispy-comte-cheesburgers-FT-RECIPE0921-6166c6552b7148e8a8561f7765ddf20b.jpg",
                               caption="Burger : $2.2",
                               reply_markup=foodChoice2)


@dp.message(F.text == "Бургер")
async def burger2(message: types.Message):
    await message.answer_photo(photo="https://www.foodandwine.com/thmb/DI29Houjc_ccAtFKly0BbVsusHc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/crispy-comte-cheesburgers-FT-RECIPE0921-6166c6552b7148e8a8561f7765ddf20b.jpg",
                               caption="Бургер : $2.2",
                               reply_markup=foodChoice2_rus)


@dp.callback_query(F.data == "burger-olish")
async def buy_burger(callback: types.CallbackQuery):
    global orders
    orders.append("Burger\n")
    await callback.message.answer("Burger savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "бургер")
async def buy2_burger(callback: types.CallbackQuery):
    global orders
    orders.append("Бургер\n")
    await callback.message.answer("Бургер добавлен в корзину", reply_markup=reception_rus)


foodChoice3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Hot-Dog sotib olish", callback_data="hot-dog-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])

foodChoice3_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купит Хот-Дог", callback_data="хот-дог"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Hot-Dog")
async def HotDog(message: types.Message):
    await message.answer_photo(photo="https://img.freepik.com/free-photo/grilled-beef-hot-dog-with-ketchup-snack-generative-ai_188544-7829.jpg",
                               caption="Hot-Dog : $2.2",
                               reply_markup=foodChoice3)


@dp.message(F.text == "Хот-Дог")
async def HotDog2(message: types.Message):
    await message.answer_photo(photo="https://img.freepik.com/free-photo/grilled-beef-hot-dog-with-ketchup-snack-generative-ai_188544-7829.jpg",
                               caption="Хот-Дог : $2.2",
                               reply_markup=foodChoice3_rus)


@dp.callback_query(F.data == "hot-dog-olish")
async def buy_HotDog(callback: types.CallbackQuery):
    global orders
    orders.append("Hot-Dog\n")
    await callback.message.answer("Hot-Dog savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "хот-дог")
async def buy2_HotDog(callback: types.CallbackQuery):
    global orders
    orders.append("Хот-Дог\n")
    await callback.message.answer("Хот-Дог добавлен в корзину", reply_markup=reception_rus)



foodChoice4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Fri sotib olish", callback_data="fri-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])

foodChoice4_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить картошку фри", callback_data="фри"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Fri")
async def fri(message: types.Message):
    await message.answer_photo(photo="https://thissillygirlskitchen.com/wp-content/uploads/2020/02/homemade-french-fries-8-1-500x375.jpg",
                               caption="Fri : $0.8",
                               reply_markup=foodChoice4)


@dp.message(F.text == "Картошка Фри")
async def fri2(message: types.Message):
    await message.answer_photo(photo="https://thissillygirlskitchen.com/wp-content/uploads/2020/02/homemade-french-fries-8-1-500x375.jpg",
                               caption="Картошка фри : $0.8",
                               reply_markup=foodChoice4_rus)


@dp.callback_query(F.data == "fri-olish")
async def buy_fri(callback: types.CallbackQuery):
    global orders
    orders.append("Fri\n")
    await callback.message.answer("Fri savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "фри")
async def buy2_fri(callback: types.CallbackQuery):
    global orders
    orders.append("Картошка фри\n")
    await callback.message.answer("Фри добавлена в корзину", reply_markup=reception_rus)


foodChoice5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Shaurma sotib olish", callback_data="shaurma-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])

foodChoice5_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить шаурму", callback_data="шаурма"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Shaurma")
async def shaurma(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3-FskJYMhZNeDxWmDs5aeZJnIzrbUs5MzLQ&s",
                               caption="Shaurma : $1.2",
                               reply_markup=foodChoice5)


@dp.message(F.text == "Шаурма")
async def shaurma2(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3-FskJYMhZNeDxWmDs5aeZJnIzrbUs5MzLQ&s",
                               caption="Шаурма : $1.2",
                               reply_markup=foodChoice5_rus)


@dp.callback_query(F.data == "shaurma-olish")
async def buy_shaurma(callback: types.CallbackQuery):
    global orders
    orders.append("Shaurma\n")
    await callback.message.answer("Shaurma savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "шаурма")
async def buy2_shaurma(callback: types.CallbackQuery):
    global orders
    orders.append("Шаурма\n")
    await callback.message.answer("Шаурма добавлена в корзину", reply_markup=reception_rus)



foodChoice6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Chizburger sotib olish", callback_data="chizburger-olish"),
     InlineKeyboardButton(text="Bekor qilish", callback_data="bekor")]

])

foodChoice6_rus = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить чизбургер", callback_data="чизбургер"),
     InlineKeyboardButton(text="Отменить", callback_data="отмена")]

])


@dp.message(F.text == "Chizburger")
async def chizburger(message: types.Message):
    await message.answer_photo(photo="https://californiadiner.ru/catalog/dvoynoy-chizburger-double-cheeseburger.jpg",
                               caption="Chizburger : $1.2",
                               reply_markup=foodChoice6)


@dp.message(F.text == "Чизбургер")
async def chizburger2(message: types.Message):
    await message.answer_photo(photo="https://californiadiner.ru/catalog/dvoynoy-chizburger-double-cheeseburger.jpg",
                               caption="Чизбургер : $1.2",
                               reply_markup=foodChoice6_rus)


@dp.callback_query(F.data == "chizburger-olish")
async def buy_chizburger(callback: types.CallbackQuery):
    global orders
    orders.append("Chizburger\n")
    await callback.message.answer("Chizburger savatga qo'shildi", reply_markup=reception)


@dp.callback_query(F.data == "чизбургер")
async def buy2_chizburger(callback: types.CallbackQuery):
    global orders
    orders.append("Чизбургер\n")
    await callback.message.answer("Чизбургер добавлен в корзину", reply_markup=reception_rus)



@dp.callback_query(F.data == "bekor")
async def back(callback: types.CallbackQuery):
    await callback.message.answer("Bekor qilindi", reply_markup=menus)


@dp.callback_query(F.data == "отмена")
async def back2(callback: types.CallbackQuery):
    await callback.message.answer("Отменено", reply_markup=menu_rus)


@dp.message(F.text == "Tilni o'zgartirish")
async def change_lang(message: types.Message):
    await message.answer("Rus tiliga o'girildi", reply_markup=reception_rus)


@dp.message(F.text == "Поменять язык")
async def change_lang(message: types.Message):
    await message.answer("Переведено на узбекский язык", reply_markup=reception)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())












































































