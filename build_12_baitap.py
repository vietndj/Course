# -*- coding: utf-8 -*-
import os

EXERCISES = [
    {
        "id": "01",
        "slug": "baitap01_laptop_ads.html",
        "title": "Soi chỉ số ads & Cày bài tập trên laptop",
        "state": "Áp lực & Căng thẳng tập trung",
        "outfit": "Âu phục blazer may đo navy",
        "avatar": "assets/marketing_baitap/viet_bt1_smartsuit.jpg",
        "frame_dir": "assets/frames_bai_tap_01",
        "voice": "Đứng một chỗ bấm máy thì nhàn thật... Nhưng lười đổi góc, khung hình nó đơ ra... thì đến mình xem lại còn muốn lướt, trách gì người ta! 😄",
        "t1": "Em đi học quay dựng là để làm video triệu view, học kỹ thuật điện ảnh cao siêu.",
        "t2": "Cầm điện thoại lên quay bạn học thì lóng ngóng, chân chôn chặt một chỗ, bấm 10 giây cho xong.",
        "t25": "Biết thừa khung hình đang chết dí một chỗ... nhưng ngại cúi thấp, sợ bạn bè bảo làm màu.",
        "t3": "Sự thật ngượng miệng: cái video mình còn chán ngấy thì ai dừng lại xem.",
        "shots": [
            ("Thiết lập áp lực bài tập", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt (0°)", "Chếch 45° bên hông trái", "Đứng một chỗ bấm máy thì nhàn thật...", "Ngồi ké bên cạnh bàn, đưa máy ngang tầm mắt cách một sải tay. Khóa nét tròng kính, lấy ánh sáng xanh màn hình hắt nhẹ lên mặt."),
            ("Ánh mắt nhíu mày sốt ruột", "02.5s - 04.5s", "Cận cảnh (CU)", "Hất nhẹ 15° từ dưới lên", "Chính diện xuyên mép laptop", "...bấm một cái là xong.", "Bước sang đối diện, hạ máy ngang mép trên màn hình laptop. Canh đúng lúc bạn nhíu mày nhìn số liệu thì bấm máy, biểu cảm thật này không diễn được đâu."),
            ("Bàn phím nhấn lì nút xóa", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 60° chúc xuống", "Từ trên xuống chếch phải", "Nhưng lười dịch cái chân, để khung hình đơ ra...", "Đưa camera sát bàn phím một gang tay, bật zoom 2x chống bóng lưng. Bắt trọn ngón tay nhấn lì nút Backspace xóa dòng chữ vừa gõ — chi tiết bế tắc đắt giá nhất."),
            ("Soi màn hình số liệu đỏ lòm", "07.0s - 09.5s", "Cận qua vai (OTS)", "Ngang vai cao 20°", "Sau lưng chếch vai phải", "...thì video dựng lên...", "Đứng chếch sau vai phải, ghé camera qua khe giữa cổ và vai áo. Lấy nét căng vào đồ thị đỏ lòm trên màn hình, tạo cảm giác nhìn lén vào áp lực thật."),
            ("Cuộn chuột & Thở dài nhẹ nhõm", "09.5s - 12.0s", "Cận góc thấp (Low ECU)", "Sát mặt bàn (0°)", "Ngang mặt bàn bên phải", "...đến mình xem lại còn lướt vội, trách gì người ta! 😄", "Đặt cạnh dưới điện thoại chạm hẳn xuống mặt bàn gỗ làm tiền cảnh. Nhắc bạn ngả người ra ghế thở hắt một hơi, kết thúc cú máy tự nhiên nhẹ nhõm.")
        ],
        "reshoots": [
            ("Bàn làm việc tại nhà ban đêm", "Chỉ bật đúng 1 bóng đèn bàn, xung quanh phòng tối om, trên bàn có cốc nước đá tan chảy hết."),
            ("Quầy thu ngân cửa hàng / kho hàng", "Đứng giữa đống thùng carton, tay cầm tập hóa đơn đối soát với màn hình máy POS."),
            ("Trên xe ô tô dừng bên lề đường", "Một tay cầm vô lăng, một tay cầm điện thoại lướt xem báo cáo doanh thu dưới ánh đèn đường vàng vọt.")
        ]
    },
    {
        "id": "02",
        "slug": "baitap02_sotay_kichban.html",
        "title": "Cuốn sổ tay & Kịch bản gạch xóa tan nát",
        "state": "Bế tắc & Tìm tòi nội tâm",
        "outfit": "Áo phông đen tối giản trẻ trung",
        "avatar": "assets/marketing_baitap/viet_bt2_tshirt.jpg",
        "frame_dir": "assets/frames_bai_tap_02",
        "voice": "Cứ tưởng đặt bút xuống là có triệu view... Đến lúc ngồi viết, gạch nát cả trang giấy... mới thấm câu: Viết cho hay thì khó, chứ viết văn mẫu thì ai cũng làm được!",
        "t1": "Em có nhiều ý tưởng lớn lắm, chỉ cần ngồi xuống là viết được kịch bản hay ngay.",
        "t2": "Cầm bút lên viết được 2 câu thì bí từ, gạch xoẹt xoẹt rồi vò đầu bứt tai, trang giấy lem luốc.",
        "t25": "Sợ bạn bè bên cạnh thấy mình ngồi cả buổi không viết nổi một câu ra hồn, nên vờ viết nguệch ngoạc để giữ thể diện.",
        "t3": "Sự thật ngượng miệng: trong đầu rỗng tuếch, toàn nhai lại văn mẫu trên mạng nên không thể tự viết được câu nào chạm vào lòng người.",
        "shots": [
            ("Trung cảnh ngồi đăm chiêu bên sổ", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt (0°)", "Chếch 30° bên phải", "Cứ tưởng đặt bút xuống là có triệu view...", "Đặt máy ngang mép bàn bên phải, bắt trọn dáng ngồi hơi gù lưng của bạn học, mắt nhìn chằm chằm trang giấy trắng."),
            ("Đầu bút bi gõ nhịp xuống mặt bàn", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn 15°", "Chính diện ngón tay", "...Đến lúc ngồi viết...", "Dí máy sát tay cầm bút một gang tay, lấy nét vào đầu bút bi đang gõ cộc cộc xuống mặt gỗ theo nhịp bối rối vô thức."),
            ("Ngòi bút gạch nát chữ Triệu View", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 70° chúc xuống", "Thẳng đứng trên trang sổ", "...gạch nát cả trang giấy...", "Chĩa máy từ trên cao chúc xuống, zoom 2x bắt nét vết mực gạch chéo dứt khoát đè lên dòng chữ kịch bản vừa viết dở."),
            ("Liếc trộm trang sổ của bạn bên cạnh", "07.0s - 09.5s", "Góc qua vai (OTS)", "Cao ngang vai 25°", "Từ sau lưng nhìn chéo sang", "...mới thấm câu: Viết cho hay thì khó...", "Đặt camera sau gáy bạn bên phải, lia chậm từ trang giấy lem luốc sang trang vở ngay ngắn của bạn ngồi kế bên."),
            ("Ném bút tựa lưng cười trừ bất lực", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Sát mặt bàn hất lên 20°", "Chính diện khuôn mặt", "...chứ viết văn mẫu thì ai cũng làm được! 😄", "Máy đặt nằm trên mặt bàn, bắt cú buông rơi cây bút xuống sổ và nụ cười tự trào mộc mạc khi nhận ra mình đang bị kẹt văn mẫu.")
        ],
        "reshoots": [
            ("Bàn góc khuất quán cà phê", "Ngồi trước cuốn sổ da mở sẵn, nhìn dòng người đi lại qua ô cửa kính mà không viết nổi một chữ."),
            ("Phòng làm việc cá nhân ban đêm", "Giấy nháp vo tròn vứt rải rác dưới chân ghế, ngồi gục trán vào hai bàn tay mỏi mệt."),
            ("Bồn rửa mặt soi gương", "Vốc một vốc nước lạnh lên mặt, ngẩng lên nhìn thẳng vào bóng mình trong gương với ánh mắt tự vấn.")
        ]
    },
    {
        "id": "03",
        "slug": "baitap03_test_goc_quay.html",
        "title": "Cầm điện thoại test góc quay tại bàn",
        "state": "Quyết liệt, Thử nghiệm & Dám làm",
        "outfit": "Đồ thể thao polo navy năng động",
        "avatar": "assets/marketing_baitap/viet_bt3_sporty.jpg",
        "frame_dir": "assets/frames_bai_tap_03",
        "voice": "Bảo giơ máy lên quay thì ai cũng ngại... Sợ run tay, sợ góc xấu, sợ người ta nhìn làm màu. Nhưng cứ bấm thử một đúp xem... xấu cũng được, miễn là mình dám bấm nút REC!",
        "t1": "Phải có máy xịn, phòng cách âm và kịch bản hoàn hảo thì em mới dám bấm máy quay.",
        "t2": "Cầm điện thoại lên quay thử thì ngượng ngùng, tay run run, mắt liếc quanh xem có ai dòm ngó mình không.",
        "t25": "Lấy cớ thiết bị chưa đủ tốt để che giấu nỗi sợ bị người khác đánh giá là vụng về, làm màu khi quay video.",
        "t3": "Sự thật ngượng miệng: sự cầu toàn chỉ là cái cớ che đậy cho thói lười biếng và nỗi sợ thất bại ngay từ bước đầu tiên.",
        "shots": [
            ("Xoay điện thoại ngắm khung hình", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang ngực 0°", "Chếch 30° trực diện", "Bảo giơ máy lên quay thì ai cũng ngại...", "Quay góc ngang ngực, bắt cử chỉ hai tay cầm điện thoại xoay ngang xoay dọc tìm góc máy chuẩn trong lớp học."),
            ("Ngón tay chạm dứt khoát nút REC đỏ", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang màn hình 20°", "Chính diện ngón cái", "...sợ run tay, sợ góc xấu, sợ người ta nhìn.", "Dí sát vào ngón tay cái tiếp xúc với màn hình cảm ứng, bắt trọn khoảnh khắc nút REC đỏ chuyển sang đếm giây 00:01."),
            ("Đặc tả cụm 3 camera phản chiếu đèn", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang lưng máy", "Chĩa thẳng ống kính", "Nhưng cứ bấm thử một đúp xem...", "Chĩa thẳng vào cụm camera sau lưng điện thoại, lấy nét căng bóng đèn tuýp lớp học phản chiếu trong tròng kính máy ảnh."),
            ("Màn hình POV quay bạn học cười ngượng", "07.0s - 09.5s", "Góc nhìn chủ quan (POV)", "Ngang tầm mắt", "Khung hình điện thoại", "...xấu cũng được...", "Góc nhìn từ người quay, thấy rõ màn hình điện thoại đang bắt nét vào bạn học đối diện đang lấy tay che miệng cười ngượng."),
            ("Hạ máy vẫy tay cười động viên", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Mặt bàn hất lên 25°", "Chính diện người quay", "...miễn là mình dám bấm nút REC! 🎬", "Đặt máy sát mặt bàn nhìn lên, bắt nụ cười rạng rỡ và bàn tay vẫy nhẹ ra hiệu: 'Được rồi đấy, đúp này tự nhiên lắm!'")
        ],
        "reshoots": [
            ("Phòng khách tại nhà", "Tự tay xoay ốc vặn chiếc chân máy tripod, gắn kẹp điện thoại và bấm nút đếm ngược 3-2-1."),
            ("Ban công ngập nắng", "Cầm sản phẩm trên tay xoay tròn trước ống kính dưới ánh nắng tự nhiên buổi sáng."),
            ("Góc phố đi bộ / quán ăn", "Đứng giữa dòng người, tự tin cầm điện thoại quay món ăn bốc khói mà không sợ ai nhìn ngó.")
        ]
    },
    {
        "id": "04",
        "slug": "baitap04_slide_giatminh.html",
        "title": "Ngẩng nhìn slide giảng bài & Giật mình",
        "state": "Vỡ òa, Thức tỉnh (Aha moment)",
        "outfit": "Sơ mi xanh nhạt xắn tay áo kiểu giảng viên",
        "avatar": "assets/marketing_baitap/viet_bt4_shirt.jpg",
        "frame_dir": "assets/frames_bai_tap_04",
        "voice": "Đang cắm đầu lướt điện thoại tưởng mình biết tuốt rồi... Nghe thầy nói một câu chạm đúng tim đen mà giật thót cả mình! Ghi vội lại... chứ không mai lại đâu đóng đấy!",
        "t1": "Mấy kiến thức này trên mạng đầy, lướt video 30 giây là hiểu hết rồi cần gì học sâu.",
        "t2": "Ngồi trong lớp nhưng cắm đầu lướt feed mạng xã hội dưới gầm bàn, mắt đảo liên tục.",
        "t25": "Giả vờ cúi đầu bấm máy như đang bận việc quan trọng, thực chất là không theo kịp bài giảng nhưng sợ hỏi lại bị chê dốt.",
        "t3": "Sự thật ngượng miệng: cái tôi quá lớn, tưởng mình giỏi hơn người khác. Đến khi bị bóc trần đúng điểm nghẽn mới thấy mình đang tự lừa dối bản thân.",
        "shots": [
            ("Cúi đầu lướt feed dưới gầm bàn", "00:00 - 02.5s", "Trung cận (MCU)", "Góc chúc 35° xuống", "Chếch phải 45°", "Đang cắm đầu lướt điện thoại tưởng mình biết tuốt rồi...", "Quay góc từ trên chúc xuống, thấy nửa người và mép điện thoại đang được lướt giấu dưới ngăn bàn học."),
            ("Ngón tay cuộn lướt bỗng khựng đơ", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mép bàn", "Chính diện màn hình", "...nghe thầy nói một câu chạm đúng tim đen...", "Cận cảnh ngón tay đang vuốt nhanh bỗng dừng khựng lại bất động, ánh sáng trắng của app hắt lên ngón tay."),
            ("Ngẩng phắt nhìn slide giật thót mình", "04.5s - 07.0s", "Cận góc thấp (Low CU)", "Hất lên 30° từ bàn", "Chếch trái nhìn bảng", "...giật thót cả mình!", "Máy đặt sát mặt bàn hất lên, bắt trọn biểu cảm mắt mở to, lông mày nhướn lên ngơ ngác khi vừa nghe một câu đâm trúng tim đen."),
            ("Hí hoáy gạch chân từ khóa vào sổ", "07.0s - 09.5s", "Đặc tả (Macro ECU)", "Góc cao 80° thẳng đứng", "Ngòi bút trên trang vở", "Ghi vội lại...", "Góc nhìn từ trên xuống ngòi bút lia nhanh 2 nét gạch chân thật đậm dưới từ khóa 'LEARN FROM FAILURE' vừa ghi vội."),
            ("Gật gù cười trừ cất hẳn điện thoại", "09.5s - 12.0s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch nghiêng 30°", "...chứ không mai lại đâu đóng đấy! 💡", "Ngang tầm mắt, bắt cử chỉ gật đầu cười thấu suốt một mình, cất hẳn chiếc điện thoại vào balo và ngồi thẳng thớm nghe giảng.")
        ],
        "reshoots": [
            ("Đang lật mở trang sách cũ", "Ngón tay lật trang sách bỗng khựng lại ở một câu trích dẫn in đậm, mắt sáng bừng lên."),
            ("Đi dạo ngoài công viên", "Bỗng dừng bước đứng khựng lại bên vỉa hè, rút vội điện thoại bật ghi âm lưu lại ý tưởng vừa nảy ra."),
            ("Bàn làm việc văn phòng", "Đang lục chồng tài liệu cũ, rút phắt ra bản kế hoạch năm ngoái và vỗ đùi đánh đét.")
        ]
    },
    {
        "id": "05",
        "slug": "baitap05_cocnuoc_langdong.html",
        "title": "Nhấp ngụm nước ấm & Tựa lưng ghế",
        "state": "Lắng đọng, Chiêm nghiệm & Kết nối chân tình",
        "outfit": "Áo len dệt kim mỏng màu be ấm áp",
        "avatar": "assets/marketing_baitap/viet_bt5_sweater.jpg",
        "frame_dir": "assets/frames_bai_tap_05",
        "voice": "Quay dựng cho đã tay rồi cũng đến lúc phải ngồi lại... Nhấp ngụm nước, nhìn lại những thước phim vụng về đầu tiên. Làm video không phải để chứng tỏ mình tài giỏi, mà là để tìm thấy những người bạn cùng tần số.",
        "t1": "Làm video là cỗ máy kiếm tiền tự động, chỉ cần tối ưu hóa chuyển đổi và phễu bán hàng.",
        "t2": "Quay xong thì mệt rã rời, ngồi một góc phòng học vắng, nhấp từng ngụm nước cho đỡ khản giọng.",
        "t25": "Gồng mình tỏ ra chuyên nghiệp suốt buổi học, đến khi mọi người về bớt mới dám thở phào, cởi bỏ chiếc mặt nạ gồng gánh.",
        "t3": "Sự thật ngượng miệng: sâu thẳm trong lòng sợ nhất là cảm giác cô đơn, làm video nhiều view mà chẳng có ai thật lòng hiểu mình.",
        "shots": [
            ("Ngồi tựa lưng ghế bên khung cửa sổ", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực 0°", "Chếch 30° đón nắng", "Quay dựng cho đã tay rồi cũng đến lúc phải ngồi lại...", "Bắt trọn dáng ngồi thư thái của anh Việt trong chiếc áo len be, nắng chiều rọi xiên vào khung cửa sổ ấm áp."),
            ("Hai bàn tay ôm trọn cốc nước ấm", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn", "Chính diện hai tay", "...Nhấp ngụm nước, nhìn lại những thước phim vụng về đầu tiên.", "Dí sát camera bắt hai bàn tay đang ủ ấm quanh chiếc cốc giấy, những ngón tay khẽ miết nhẹ thân cốc thong thả."),
            ("Đặc tả miệng cốc nước bốc hơi nhẹ", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang miệng cốc", "Chếch ngược sáng", "Làm video không phải để chứng tỏ mình tài giỏi...", "Lấy nét căng vào làn khói mỏng bốc lên từ miệng cốc dưới vệt nắng chiều, tạo điểm dừng thị giác êm đềm."),
            ("Khung cảnh lớp học dần vắng người", "07.0s - 09.5s", "Góc nhìn rộng (Wide OTS)", "Ngang vai", "Hướng ra dãy bàn ghế", "...mà là để tìm thấy những người bạn...", "Góc nhìn từ sau lưng nhân vật nhìn bao quát không gian phòng học sau giờ tan lớp, bàn ghế ngay ngắn tĩnh lặng."),
            ("Nụ cười nhẹ nhõm bình an nhìn thẳng", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện ống kính", "...cùng tần số với mình! ☕", "Bắt trọn nụ cười mộc mạc không phòng thủ, ánh mắt chân thành như đang ngồi đối diện trò chuyện cùng một người bạn tri kỷ.")
        ],
        "reshoots": [
            ("Ban công chung cư lúc hoàng hôn", "Ngồi tựa ghế mây, hai tay cầm tách trà nóng nhìn dòng xe cộ phía dưới, gió thổi nhẹ vạt áo."),
            ("Bàn ăn gia đình buổi tối", "Sau khi dọn dẹp bát đĩa xong, ngồi tựa vào ghế nhâm nhi một tách trà thảo mộc bên ngọn đèn trần ấm áp."),
            ("Ghế đá công viên sáng sớm", "Ngồi một mình thong thả hít thở không khí trong lành dưới tán cây xanh mát, gác lại mọi âu lo.")
        ]
    },
    {
        "id": "06",
        "slug": "baitap06_do_du_nut_dang.html",
        "title": "Ngón tay ngập ngừng trước nút Đăng bài",
        "state": "Do dự, Nghi ngờ & Đấu tranh nội tâm",
        "outfit": "Áo khoác denim bụi bặm",
        "avatar": "assets/marketing_baitap/viet_bt6_denim.jpg",
        "frame_dir": "assets/frames_bai_tap_06",
        "voice": "Người lớn mình buồn cười lắm... Soạn xong kịch bản rồi, ngón tay đặt lên nút Đăng thì cứ run lên vì sợ: 'Liệu người ta có chê mình làm trò không?'. Không bấm thì an toàn thật, nhưng sẽ mãi đứng nguyên một chỗ!",
        "t1": "Em là người kỹ tính, em chưa đăng vì muốn chuẩn bị thêm vài tài liệu nữa cho nó chu toàn.",
        "t2": "Màn hình đã load sẵn nút Xuất bản màu xanh, nhưng ngón tay cứ giơ lên rồi lại hạ xuống cả chục lần.",
        "t25": "Sợ bạn bè cùng trang lứa, đồng nghiệp cũ nhìn thấy mình làm video rồi xì xào bàn tán: 'Dạo này rảnh rỗi bày đặt lên mạng dạy đời'.",
        "t3": "Sự thật ngượng miệng: lòng tự ái quá lớn, sợ nhận về sự thờ ơ hoặc vài ba lời bình luận châm chọc khiến mình bị bẽ mặt.",
        "shots": [
            ("Ngồi trầm ngâm cầm điện thoại hai tay", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 35° bên trái", "Người lớn mình buồn cười lắm...", "Bắt trọn ánh mắt đăm chiêu giằng xé của anh Việt trong chiếc áo khoác denim, hai tay nâng điện thoại sát mặt bàn."),
            ("Ngón tay trỏ ngập ngừng cách nút Đăng 1mm", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang màn hình", "Chính diện ngón trỏ", "...Soạn xong kịch bản rồi, ngón tay đặt lên nút Đăng...", "Dí sát vào ngón tay đang run nhẹ, nhấp nhả 2 nhịp ngay trên nút bấm màu xanh nhưng không dám chạm xuống."),
            ("Đặc tả nút Đăng nhấp nháy trên màn hình", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Cận cảnh giao diện", "...thì cứ run lên vì sợ: 'Liệu người ta có chê mình làm trò không?'", "Khóa nét vào chữ 'Đăng video' sắc nét trên giao diện ứng dụng, tạo cảm giác nghẹt thở của khoảnh khắc quyết định."),
            ("Liếc mắt nhìn quanh phòng học", "07.0s - 09.5s", "Góc nhìn môi trường (OTS)", "Ngang cằm", "Quét sang bạn bè", "Không bấm thì an toàn thật...", "Góc nhìn từ sau lưng liếc nhẹ sang những bạn học xung quanh đang trò chuyện, phản ánh nỗi sợ bị dòm ngó."),
            ("Hạ máy úp màn hình xuống mặt bàn", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Mặt bàn hất lên 15°", "Chính diện khuôn mặt", "...nhưng sẽ mãi đứng nguyên một chỗ!", "Úp mạnh chiếc điện thoại xuống mặt bàn gỗ cạch một cái, ngẩng mặt lên thở dài tự vấn: 'Rốt cuộc mình đang sợ cái gì?'")
        ],
        "reshoots": [
            ("Trước cửa phòng họp công ty", "Tay cầm tập hồ sơ đưa lên định gõ cửa gặp sếp đề xuất ý tưởng mới rồi lại rụt tay xuống chỉnh áo."),
            ("Ngồi trong xe ô tô trước sự kiện", "Nhìn vào gương chiếu hậu chỉnh lại tóc tai, hít sâu một hơi rồi chần chừ mở cửa xe."),
            ("Màn hình máy tính thanh toán", "Con chuột máy tính di qua di lại giữa hai nút 'Xác nhận thanh toán' và 'Hủy bỏ' khóa học.")
        ]
    },
    {
        "id": "07",
        "slug": "baitap07_hut_hang_0view.html",
        "title": "Mở máy kiểm tra thấy 0 view, tụt mood",
        "state": "Hụt hẫng, Thất vọng & Va vào thực tế",
        "outfit": "Áo hoodie xám tối giản",
        "avatar": "assets/marketing_baitap/viet_bt7_hoodie.jpg",
        "frame_dir": "assets/frames_bai_tap_07",
        "voice": "Lúc mới làm, ai cũng mơ về video triệu view với nghìn đơn. Mở máy ra thấy đúng 3 lượt xem, trong đó có 2 lượt mình tự bấm... Lúc ấy mới hiểu: Nghề này không có chỗ cho kẻ há miệng chờ sung!",
        "t1": "Video này thuật toán bóp tương tác rồi, chứ nội dung em làm hay thế này ai chả thích.",
        "t2": "Mở ứng dụng ra kéo vuốt liên tục để refresh, nhưng con số lượt xem vẫn đứng im lìm ở mức 0 tròn trĩnh.",
        "t25": "Hôm qua vừa hào hứng khoe với mọi người là sắp bùng nổ, hôm nay số liệu tụt dốc thê thảm, xấu hổ chỉ muốn xóa kênh đi cho đỡ ngượng.",
        "t3": "Sự thật ngượng miệng: vỡ mộng vì nhận ra mình chẳng có sức hút như mình tự tưởng tượng; đối mặt với cảm giác mình thật tầm thường.",
        "shots": [
            ("Ngồi gục vai nhìn màn hình điện thoại", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang ngực", "Chính diện bàn học", "Lúc mới làm, ai cũng mơ về video triệu view với nghìn đơn.", "Anh Việt trong chiếc áo hoodie xám ngồi trĩu hai vai xuống bàn, ánh sáng yếu ớt của màn hình chiếu lên khuôn mặt bất động."),
            ("Hai cánh tay buông thõng trên mặt bàn", "02.5s - 04.5s", "Cận cảnh (CU)", "Góc nghiêng 20°", "Dọc theo cánh tay", "...Mở máy ra thấy đúng 3 lượt xem...", "Góc máy dọc theo hai cánh tay buông xuôi bất lực trên mặt bàn gỗ, những ngón tay xòe ra không còn chút sức lực."),
            ("Đặc tả màn hình hiển thị 0 Lượt xem", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Chính diện con số", "...trong đó có 2 lượt mình tự bấm...", "Lấy nét căng vào dòng chữ '0 Lượt xem • 0 Bình luận' trơ trọi trên nền trắng của ứng dụng, sự thật phũ phàng."),
            ("Không gian lớp học vắng lặng bao quanh", "07.0s - 09.5s", "Góc cao (High Angle)", "Chúc 45° từ trên xuống", "Toàn cảnh bàn học", "Lúc ấy mới hiểu: Nghề này...", "Máy đặt trên cao nhìn xuống chiếc điện thoại nằm đơn độc giữa mặt bàn học rộng thênh thang, cảm giác lạc lõng cùng cực."),
            ("Khuôn mặt nghệt ra rồi khẽ lắc đầu", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện", "...không có chỗ cho kẻ há miệng chờ sung! 🌧️", "Bắt trọn cái lắc đầu nhẹ, khóe môi khẽ nhếch cười tự giễu: 'Tốt lắm, coi như ăn một cái tát để tỉnh ngủ mà làm lại từ đầu!'")
        ],
        "reshoots": [
            ("Cửa hàng vắng khách ngày mưa", "Đứng tựa quầy thu ngân nhìn ra ngoài trời mưa tầm tã, không một bóng khách ghé vào."),
            ("Bàn làm việc cuối tháng", "Cầm tờ sao kê tài khoản hoặc hóa đơn tiền thuê mặt bằng, ánh mắt đờ đẫn nhìn vào khoảng không vô định."),
            ("Băng ghế đá công viên", "Ngồi nhìn xuống đôi giày dính bụi sau một ngày dài đi chào hàng nhưng toàn bị từ chối thẳng thừng.")
        ]
    },
    {
        "id": "08",
        "slug": "baitap08_qua_ngot_tingting.html",
        "title": "Ting ting thông báo tin nhắn & Đơn đầu tiên",
        "state": "Tự hào, Nhẹ nhõm & Quả ngọt đầu tiên",
        "outfit": "Áo sơ mi kẻ caro nhã nhặn",
        "avatar": "assets/marketing_baitap/viet_bt8_plaid.jpg",
        "frame_dir": "assets/frames_bai_tap_08",
        "voice": "Tiếng ting ting nổ tin nhắn đầu tiên... giá trị nó chẳng đáng bao nhiêu tiền đâu. Nhưng nó đập tan mọi nỗi sợ trước đó: Phương pháp này có thật, và mình hoàn toàn làm được!",
        "t1": "Mới được có một tin nhắn, có gì đâu mà phải mừng, phải tiền tỷ mới đáng nói.",
        "t2": "Màn hình điện thoại bất ngờ sáng bừng lên giữa giờ học, banner tin nhắn khách hỏi mua hàng hiện lên rõ mồn một.",
        "t25": "Muốn nhảy cẫng lên ăn mừng nhưng sợ cả lớp nhìn bảo trẻ trâu, đành cắn chặt môi cố kìm nén nụ cười đắc chí.",
        "t3": "Sự thật ngượng miệng: suốt bao lâu nay luôn tự ti nghĩ mình bất tài vô dụng, khoảnh khắc này mới chính thức giải oan cho lòng tự trọng của bản thân.",
        "shots": [
            ("Ngồi thẳng lưng mắt dán vào màn hình sáng", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 30° bên phải", "Tiếng ting ting nổ tin nhắn đầu tiên...", "Anh Việt trong áo sơ mi kẻ caro ngồi thẳng thớm, ánh mắt bỗng mở to ngạc nhiên nhìn chằm chằm vào chiếc điện thoại vừa rung lên."),
            ("Hai bàn tay nâng vội chiếc điện thoại", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang ngực", "Chính diện hai bàn tay", "...giá trị nó chẳng đáng bao nhiêu tiền đâu.", "Cận cảnh hai bàn tay vội vã nhấc máy lên, ngón tay cái lướt nhẹ mở khóa màn hình với vẻ nâng niu trân trọng."),
            ("Đặc tả banner tin nhắn khách hàng chốt đơn", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Lấy nét banner thông báo", "Nhưng nó đập tan mọi nỗi sợ trước đó...", "Lấy nét căng vào dòng thông báo: 'New Customer Message: Em muốn đăng ký học ngay ạ...' nổi bật trên nền màn hình khóa."),
            ("Xoay màn hình khoe bạn ngồi bên cạnh", "07.0s - 09.5s", "Góc nhìn hai người (Two-shot)", "Ngang vai", "Lia sang bạn kế bên", "Phương pháp này có thật...", "Lia máy bắt khoảnh khắc anh Việt huých nhẹ vai bạn học bên cạnh, xoay chiếc điện thoại sang khoe: 'Này, có khách nhắn thật rồi!'"),
            ("Nụ cười rạng rỡ nắm chặt tay ăn mừng", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt hất nhẹ", "Chính diện", "...và mình hoàn toàn làm được! 🎉", "Bắt trọn nụ cười rạng rỡ hạnh phúc, bàn tay nắm chặt kéo giật về phía sau theo phản xạ ăn mừng thầm lặng đầy kiêu hãnh.")
        ],
        "reshoots": [
            ("Quán cà phê sáng sớm", "Nghe tiếng chuông ting ting báo tiền về tài khoản, mỉm cười nhấc ly cà phê lên nhấp một ngụm đầy sảng khoái."),
            ("Bàn đóng gói hàng tại nhà", "Tự tay dán băng dính lên thùng hàng đầu tiên gửi đi cho khách, cẩn thận miết phẳng từng mép hộp carton."),
            ("Góc ban công ngập nắng", "Cầm điện thoại xem video của mình vừa cán mốc 10.000 view đầu tiên, gió lay nhẹ vạt áo, nụ cười tự hào bình dị.")
        ]
    },
    {
        "id": "09",
        "slug": "baitap09_timeline_capcut.html",
        "title": "Đeo tai nghe soi timeline CapCut cắt gọt",
        "state": "Tỉ mỉ, Cầu toàn & Tận tâm kỹ thuật",
        "outfit": "Áo thun đen tối giản + Tai nghe over-ear",
        "avatar": "assets/marketing_baitap/viet_bt9_headphones.jpg",
        "frame_dir": "assets/frames_bai_tap_09",
        "voice": "Cắt đi nửa giây thừa, kéo lại một nhịp thở... Người xem không biết bạn tỉ mỉ thế nào sau bàn dựng đâu. Nhưng họ sẽ ở lại trọn vẹn video, đơn giản vì không có một giây nào bị thừa thãi!",
        "t1": "Dựng video cứ cắt bừa chèn hiệu ứng giật giật vào là người ta xem, quan tâm gì tiểu tiết.",
        "t2": "Đeo tai nghe kín mít, phóng to timeline lên từng khung hình 30fps, tua đi tua lại một đoạn thoại đúng 10 lần.",
        "t25": "Cố tình đeo tai nghe xịn, ngồi gõ phím cành cạch để ra vẻ dân editor chuyên nghiệp giữa lớp học.",
        "t3": "Sự thật ngượng miệng: sợ bị chê là thợ cắt ghép thô thiển, sợ video của mình bị đánh giá là rẻ tiền nên phải soi từng mili-giây để tự bảo vệ lòng tự trọng nghề nghiệp.",
        "shots": [
            ("Ngồi chăm chú bên laptop và tai nghe chụp tai", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 45° bên trái", "Cắt đi nửa giây thừa, kéo lại một nhịp thở...", "Bắt trọn thần thái tập trung cao độ của anh Việt với chiếc tai nghe Sony trùm đầu, màn hình laptop hiển thị giao diện dựng phim chuyên nghiệp."),
            ("Màn hình laptop với timeline nhiều layer", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang bàn phím", "Chếch nhìn màn hình", "...Người xem không biết bạn tỉ mỉ thế nào...", "Lấy nét vào màn hình MacBook hiển thị timeline CapCut với các dải màu tím, xanh lá của âm thanh và video được cắt gọt tinh xảo."),
            ("Đặc tả ngón tay bấm phím cắt đúp thừa", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 60°", "Chính diện bàn phím", "...sau bàn dựng đâu...", "Khóa nét ngón trỏ và ngón cái nhấn tổ hợp phím Command + B, nhát cắt sắc lẹm chia đôi đoạn video thừa thãi trên timeline."),
            ("Ánh mắt tập trung soi chuyển động từng frame", "07.0s - 09.5s", "Cận cảnh ánh mắt (CU Eyes)", "Ngang tầm mắt", "Chính diện", "Nhưng họ sẽ ở lại trọn vẹn video...", "Cận cảnh đôi mắt chăm chú phản chiếu ánh sáng nhấp nháy từ màn hình máy tính, lông mày giãn nhẹ khi tìm đúng điểm nối cảnh raccord."),
            ("Gật gù nhịp chân theo tiếng nhạc nền", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Sát mặt bàn hất lên", "Chếch 30°", "...vì không có một giây nào bị thừa thãi! 🎧", "Bắt cử chỉ gật gù hài lòng theo nhịp điệu âm thanh trong tai nghe, ngón tay gõ nhẹ lên mép máy tính báo hiệu một đúp dựng hoàn hảo.")
        ],
        "reshoots": [
            ("Phòng dựng phim tại nhà ban đêm", "Ngồi trước màn hình đôi 27 inch trong phòng tối, bàn phím cơ phát sáng lung linh, tay lia chuột mượt mà."),
            ("Quán cà phê yên tĩnh", "Ngồi góc bàn dài, cắm tai nghe vào laptop cặm cụi dựng video giữa tiếng nhạc nền du dương của quán."),
            ("Băng ghế chờ sân bay", "Mở laptop tranh thủ render nốt video trước giờ lên máy bay, ánh mắt chạy đua với thời gian.")
        ]
    },
    {
        "id": "10",
        "slug": "baitap10_tranh_luan_nhom.html",
        "title": "Chụm đầu tranh luận kịch bản với bạn học",
        "state": "Va chạm quan điểm & Tinh thần đồng đội",
        "outfit": "Áo blazer linen trẻ trung",
        "avatar": "assets/marketing_baitap/viet_bt10_blazer.jpg",
        "frame_dir": "assets/frames_bai_tap_10",
        "voice": "Ngồi một mình thì tưởng ý tưởng của mình là nhất. Đến lúc đem ra bàn luận với anh em, người ta bóc cho vài câu mới thấy hổng toe toét. Nhưng có cọ xát thì mới gọt sắc được thông điệp!",
        "t1": "Ý tưởng của em độc quyền, em không muốn chia sẻ vì sợ bị người khác sao chép.",
        "t2": "Mấy anh em chụm đầu vào nhau quanh bàn học, ngón tay chỉ lia lịa vào từng dòng chữ, cãi nhau chí choé về đoạn mở đầu.",
        "t25": "Ban đầu gồng lên bảo vệ ý kiến của mình vì sợ nhận sai trước mặt mọi người, nhưng trong bụng biết thừa luận điểm của bạn có lý hơn.",
        "t3": "Sự thật ngượng miệng: cái tôi bảo thủ, sợ bị bóc mẽ là tư duy non nớt; nhưng khi dám mở lòng lắng nghe thì mới vỡ lẽ ra bao nhiêu điều hay ho.",
        "shots": [
            ("Cúi người đứng chỉ tay vào trang kịch bản", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 35° giữa hai người", "Ngồi một mình thì tưởng ý tưởng của mình là nhất.", "Anh Việt trong chiếc áo blazer linen cúi người trên bàn học, tay chỉ thẳng vào trang giấy kịch bản đang mở sẵn trước mặt bạn học."),
            ("Bàn tay chỉ vào dòng chữ gạch đầu dòng", "02.5s - 04.5s", "Cận cảnh (CU)", "Góc nghiêng 45°", "Mặt bàn học", "Đến lúc đem ra bàn luận với anh em...", "Dí sát camera bắt ngón tay trỏ đang gõ nhẹ vào một dòng chữ chìa khóa, bạn ngồi bên cạnh cũng đặt tay lên mép vở lắng nghe."),
            ("Đặc tả nét vẽ sơ đồ 4 bước trên giấy", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng 80°", "Chính diện trang sổ", "...người ta bóc cho vài câu mới thấy hổng toe toét...", "Lấy nét căng vào sơ đồ mũi tên vẽ tay nối các ô 'Hook ➔ Nỗi đau ➔ Bẻ lái ➔ Hành động' đầy sống động trên trang giấy kẻ ô."),
            ("Góc nhìn hai khuôn mặt cùng hướng về một điểm", "07.0s - 09.5s", "Góc hai người (Two-shot)", "Ngang cằm", "Bắt tương tác hai bên", "Nhưng có cọ xát...", "Bắt biểu cảm của bạn học đang gật gù ngẫm nghĩ, đối chiếu với nụ cười cởi mở đầy năng lượng của anh Việt đang giải thích."),
            ("Đập tay tán thưởng chốt xong phương án", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Hất lên từ mép bàn", "Chính diện", "...thì mới gọt sắc được thông điệp! 🤝", "Bắt trọn khoảnh khắc hai bàn tay đập nhẹ vào nhau (High-five) trên mặt bàn, nụ cười đồng thuận rạng rỡ: 'Chốt kịch bản này, bao cuốn!'")
        ],
        "reshoots": [
            ("Phòng họp brainstorm công ty", "Đứng trước tấm bảng kính vẽ đầy sơ đồ mindmap, cùng đồng nghiệp tranh luận về chiến dịch ra mắt sản phẩm."),
            ("Bàn tròn quán trà sữa / cafe", "3-4 bạn trẻ ngồi quây quần cùng chiếc laptop, vừa ăn bánh vừa hào hứng vẽ storyboard lên khăn giấy."),
            ("Góc ban công thảo luận ngoài trời", "Hai người đứng tựa lan can, một người cầm kịch bản đọc to, người kia góp ý từng câu thoại.")
        ]
    },
    {
        "id": "11",
        "slug": "baitap11_tap_noi_truoc_lop.html",
        "title": "Đứng trước lớp tập nói đúp quay đầu tiên",
        "state": "Vượt qua nỗi sợ & Can đảm trước đám đông",
        "outfit": "Áo sơ mi trắng cổ bẻ lịch thiệp",
        "avatar": "assets/marketing_baitap/viet_bt11_whiteshirt.jpg",
        "frame_dir": "assets/frames_bai_tap_11",
        "voice": "Đứng trước ống kính mà run như cầy sấy thì ai cũng từng trải qua. Nhưng nuốt nước bọt một cái, nhìn thẳng vào mắt camera và mở lời... Qua được đúp quay đầu tiên này là bạn đã thắng 90% người ngoài kia rồi!",
        "t1": "Em là người hướng nội, em chỉ hợp làm nội dung dạng chữ chứ không bao giờ đứng nói trước ống kính được.",
        "t2": "Đứng trước chiếc điện thoại gắn trên chân máy mini, cổ họng nghẹn ứ, hai tay nắm chặt mép bàn học, nuốt nước bọt ừng ực.",
        "t25": "Cố gắng tỏ ra đĩnh đạc tự tin trước mặt các bạn trong lớp, nhưng tim đập thình thịch như muốn nhảy ra khỏi lồng ngực.",
        "t3": "Sự thật ngượng miệng: sợ bị chê là mặt đơ, giọng nói quê mùa, sợ người quen nhìn thấy sẽ cười cợt sau lưng mình.",
        "shots": [
            ("Đứng cạnh bảng trắng đối diện chân máy phone", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 30° trực diện", "Đứng trước ống kính mà run như cầy sấy thì ai cũng từng trải qua.", "Anh Việt trong chiếc áo sơ mi trắng tinh tươm đứng bên bảng lớp học, hai tay mở nhẹ với cử chỉ tự nhiên, đối diện chiếc điện thoại kẹp tripod."),
            ("Chiếc điện thoại kẹp ngay ngắn trên tripod mini", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn", "Chính diện chân máy", "Nhưng nuốt nước bọt một cái...", "Lấy nét căng vào chiếc chân máy tripod 3 chân nhỏ gọn đặt vững chãi trên mặt bàn, kẹp chiếc điện thoại đang ở chế độ chờ."),
            ("Đặc tả camera điện thoại đếm ngược 3... 2... 1", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang ống kính", "Chĩa thẳng mắt camera", "...nhìn thẳng vào mắt camera và mở lời...", "Khóa nét vào cụm mắt camera điện thoại phản chiếu ánh sáng phòng học, chấm đèn đỏ nhấp nháy báo hiệu chuẩn bị ghi hình."),
            ("Không gian phòng học nhìn từ bục giảng", "07.0s - 09.5s", "Góc toàn qua vai (Wide OTS)", "Từ sau vai người nói", "Hướng xuống lớp học", "Qua được đúp quay đầu tiên này...", "Góc nhìn từ sau lưng nhân vật bao quát các dãy bàn học và các bạn sinh viên đang chăm chú dõi theo, không gian rộng mở."),
            ("Thở phào nhẹ nhõm mỉm cười tự tin", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện", "...là bạn đã thắng 90% người ngoài kia rồi! 🎙️", "Bắt trọn nụ cười bừng sáng và hơi thở phào nhẹ nhõm của anh Việt ngay sau khi hoàn thành đúp nói: 'Thấy chưa, có chết ai đâu!'")
        ],
        "reshoots": [
            ("Phòng khách tại nhà tự quay", "Đứng trước góc tường trắng phòng khách, tự bấm máy quay clip chia sẻ kinh nghiệm đầu tiên trong đời."),
            ("Hội trường / Sân khấu nhỏ", "Đứng trên bục phát biểu cầm micro, nhìn xuống hàng ghế khán giả và tự tin chia sẻ câu chuyện của mình."),
            ("Góc vườn / Công viên ngoài trời", "Cầm gậy selfie đi dạo vừa đi vừa nói chuyện với camera một cách tự nhiên như tâm sự với bạn hiền.")
        ]
    },
    {
        "id": "12",
        "slug": "baitap12_thu_don_buoc_di.html",
        "title": "Gập laptop, đeo balo bước ra khỏi lớp",
        "state": "Giải phóng, Tự tin & Sẵn sàng thực chiến",
        "outfit": "Áo gió thể thao / Bomber jacket năng động",
        "avatar": "assets/marketing_baitap/viet_bt12_windbreaker.jpg",
        "frame_dir": "assets/frames_bai_tap_12",
        "voice": "Học xong một buổi, đầu nảy số hàng tá ý tưởng. Gập máy lại, bước ra khỏi phòng học... Giờ không còn là bài tập trên lớp nữa, mà là bước ra ngoài đời để tự tay làm ra kết quả thật!",
        "t1": "Học xong khóa học này là mình thành bậc thầy làm video rồi, ngồi chờ tiền tự chảy về túi.",
        "t2": "Thu dọn sổ bút, gập chiếc laptop lại, khoác chiếc balo lên vai, hít một hơi thật sâu chào các bạn rồi bước ra cửa.",
        "t25": "Hết giờ học cảm thấy người nhẹ nhõm hẳn vì không còn phải chịu áp lực bài vở, nhưng trong lòng bắt đầu le lói cảm giác sốt ruột muốn về làm thử ngay.",
        "t3": "Sự thật ngượng miệng: hiểu rằng kiến thức trong lớp chỉ là 10%, nếu về nhà không chịu cầm máy lên làm thì mãi mãi chỉ là kẻ nói phét lý thuyết suông.",
        "shots": [
            ("Đứng bên cánh cửa lớp khoác balo trên vai", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 30° khung cửa", "Học xong một buổi, đầu nảy số hàng tá ý tưởng.", "Anh Việt trong chiếc áo gió thể thao năng động, một bên vai đeo chiếc balo đen, đứng ngay mép cửa lớp học với ánh mắt hướng về phía trước."),
            ("Bàn tay gập nắp laptop MacBook êm ái", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mép bàn", "Chính diện bàn tay", "Gập máy lại...", "Lấy nét vào bàn tay đặt lên góc trên nắp máy tính, hạ nhẹ nắp màn hình xuống nghe tiếng 'tách' hít nam châm quen thuộc."),
            ("Đặc tả chiếc khóa kéo balo được kéo gọn gàng", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang thân balo", "Chính diện đường khóa", "...bước ra khỏi phòng học...", "Dí sát camera bắt ngón tay kéo dứt khoát chiếc khóa kéo kim loại trên chiếc balo đen, đóng gói trọn vẹn đồ đạc tác nghiệp."),
            ("Dãy hành lang lớp học ngập tràn ánh sáng", "07.0s - 09.5s", "Góc nhìn phối cảnh (POV/Wide)", "Ngang tầm mắt", "Hướng ra hành lang", "Giờ không còn là bài tập trên lớp nữa...", "Khung cảnh hành lang trường học dài thênh thang ngập nắng ban ngày, mở ra không gian rộng lớn của đời thực."),
            ("Quay đầu lại mỉm cười vẫy tay chào tạm biệt", "09.5s - 12.0s", "Trung cận (MCU)", "Ngang tầm mắt", "Nhìn lại ống kính", "...mà là bước ra ngoài đời để tự tay làm ra kết quả thật! 🚀", "Anh Việt quay nửa người lại, nở nụ cười hào sảng, vẫy tay chào lớp học đầy năng lượng rồi sải bước tiến về phía trước.")
        ],
        "reshoots": [
            ("Rời khỏi quán cà phê sau buổi làm việc", "Đứng dậy đeo túi, cầm cốc nước trả quầy rồi bước ra đường phố tấp nập trong ánh chiều buông."),
            ("Cửa thang máy tòa nhà văn phòng", "Bước vào thang máy bấm nút xuống tầng hầm, ngắm nhìn hình ảnh mình tràn đầy quyết tâm trong gương thang máy."),
            ("Sải bước trên cầu vượt bộ hành", "Đeo tai nghe, sải bước dài trên cầu vượt nhìn xuống dòng xe cộ hối hả, tâm thế sẵn sàng chinh phục mục tiêu mới.")
        ]
    }
]

TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Bài Tập {id} • {title} | Kho Kịch Bản Marketing Thực Chiến</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&family=Playfair+Display:ital,wght@1,600;1,700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --cl-bg-light: #ffffff;
      --cl-bg-tint: #f8fafc;
      --cl-text-main: #0f172a;
      --cl-text-sub: #334155;
      --cl-text-muted: #64748b;
      --cl-accent: #1a73e8;
      --cl-accent-hover: #1557b0;
      --cl-border: rgba(0, 0, 0, 0.08);
      --cl-card-bg: #ffffff;
      --apple-spring: cubic-bezier(0.25, 1, 0.35, 1.05);
      --apple-ease: cubic-bezier(0.16, 1, 0.3, 1);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--cl-bg-light);
      color: var(--cl-text-main);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Sticky Navigation */
    .sticky-nav {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--cl-border);
      padding: 12px 24px;
      display: flex; justify-content: space-between; align-items: center; gap: 16px;
    }}
    .nav-brand {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: inherit; }}
    .brand-badge {{
      background: var(--cl-accent); color: #fff; font-size: 10.5px; font-weight: 800;
      padding: 4px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .nav-title {{ font-size: 13.5px; font-weight: 700; color: var(--cl-text-main); }}
    .nav-actions {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .nav-link-btn {{
      background: var(--cl-bg-tint); border: 1px solid var(--cl-border); color: var(--cl-text-sub);
      font-size: 12px; font-weight: 600; padding: 6px 12px; border-radius: 8px; text-decoration: none; transition: all 0.2s;
    }}
    .nav-link-btn:hover, .nav-link-btn.active {{
      background: var(--cl-accent); color: #fff; border-color: var(--cl-accent);
    }}
    .nav-select {{
      background: #fff; border: 1px solid var(--cl-border); color: var(--cl-text-main);
      font-size: 12px; font-weight: 600; padding: 6px 10px; border-radius: 8px; outline: none; cursor: pointer;
    }}

    /* Zebra Sections */
    .cl-zebra-section {{
      width: 100%;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px 24px;
      position: relative;
    }}
    .cl-zebra--light {{ background-color: var(--cl-bg-light); }}
    .cl-zebra--tint {{
      background-color: var(--cl-bg-tint);
      border-top: 1px solid var(--cl-border);
      border-bottom: 1px solid var(--cl-border);
    }}

    .cl-container {{
      max-width: 1240px;
      margin: 0 auto;
      width: 100%;
    }}

    /* Typography */
    .cl-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 100px;
      background: rgba(26, 115, 232, 0.08);
      color: var(--cl-accent);
      border: 1px solid rgba(26, 115, 232, 0.2);
      margin-bottom: 18px;
    }}
    .title-short {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(28px, 4vw, 44px);
      font-weight: 800;
      line-height: 1.25;
      color: var(--cl-text-main);
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    .title-long {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(22px, 2.8vw, 32px);
      font-weight: 700;
      line-height: 1.35;
      color: var(--cl-text-main);
      margin-bottom: 14px;
    }}
    .editorial-quote {{
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: clamp(18px, 2vw, 22px);
      line-height: 1.6;
      color: #b45309;
      background: #fffbeb;
      padding: 16px 20px;
      border-radius: 12px;
      border-left: 4px solid #f59e0b;
      margin: 18px 0;
    }}
    .cl-lead {{
      font-size: clamp(16px, 1.4vw, 18px);
      color: var(--cl-text-sub);
      max-width: 880px;
      line-height: 1.8;
      margin-bottom: 24px;
    }}

    /* Apple Reveal Animation */
    .apple-reveal {{
      opacity: 0;
      transform: translate3d(0, 24px, 0);
      transition: opacity 0.6s var(--apple-ease), transform 0.65s var(--apple-spring);
      will-change: opacity, transform;
    }}
    .apple-reveal.is-visible {{
      opacity: 1;
      transform: translate3d(0, 0, 0);
    }}

    /* Hero Layout */
    .hero-split {{
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 40px;
      align-items: center;
    }}
    @media (max-width: 980px) {{
      .hero-split {{ grid-template-columns: 1fr; }}
    }}

    .hero-avatar-box {{
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      aspect-ratio: 9 / 16;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
      border: 1px solid var(--cl-border);
      background: #000;
    }}
    .hero-avatar-box img {{
      width: 100%; height: 100%; object-fit: cover;
    }}
    .hero-avatar-badge {{
      position: absolute; bottom: 14px; left: 14px; right: 14px;
      background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 10px;
      padding: 10px 14px; color: #fff;
    }}
    .avatar-tag {{ font-size: 10px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px; }}
    .avatar-name {{ font-size: 13px; font-weight: 800; }}

    /* Master Voice Card */
    .voice-action-card {{
      background: #ffffff;
      border: 1px solid #bfdbfe;
      border-radius: 16px;
      padding: 20px 24px;
      margin-top: 24px;
      box-shadow: 0 4px 20px rgba(26, 115, 232, 0.08);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .voice-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .voice-badge {{
      font-size: 11px;
      font-weight: 800;
      color: var(--cl-accent);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .copy-voice-btn {{
      background: var(--cl-accent);
      color: #ffffff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background 0.2s;
    }}
    .copy-voice-btn:hover {{ background: var(--cl-accent-hover); }}
    .voice-text-box {{
      font-size: 16px;
      font-weight: 600;
      color: #1e293b;
      line-height: 1.6;
      font-style: italic;
    }}

    /* 4 Tiers of Truth Cards Grid */
    .tiers-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 28px;
    }}
    @media (max-width: 1024px) {{ .tiers-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 600px) {{ .tiers-grid {{ grid-template-columns: 1fr; }} }}

    .tier-apple-card {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 16px;
      padding: 22px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
      transition: transform 0.2s var(--apple-spring), box-shadow 0.2s;
    }}
    .tier-apple-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.08);
    }}
    .tier-apple-card.t1 {{ border-top: 4px solid #ef4444; }}
    .tier-apple-card.t2 {{ border-top: 4px solid #f59e0b; }}
    .tier-apple-card.t25 {{ border-top: 4px solid #8b5cf6; background: linear-gradient(180deg, #faf5ff 0%, #ffffff 100%); }}
    .tier-apple-card.t3 {{ border-top: 4px solid #10b981; }}

    .tier-label {{ font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; }}
    .t1 .tier-label {{ color: #dc2626; }}
    .t2 .tier-label {{ color: #d97706; }}
    .t25 .tier-label {{ color: #7c3aed; }}
    .t3 .tier-label {{ color: #059669; }}

    .tier-desc {{ font-size: 14px; color: var(--cl-text-sub); line-height: 1.6; flex: 1; }}
    .tier-subnote {{
      font-size: 11.5px; color: var(--cl-text-muted); line-height: 1.5; border-top: 1px dashed var(--cl-border); padding-top: 8px; margin-top: 4px;
    }}

    /* 5 Beats Storyboard Grid */
    .storyboard-grid-5 {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      margin-top: 24px;
    }}
    @media (max-width: 1200px) {{ .storyboard-grid-5 {{ grid-template-columns: repeat(3, 1fr); }} }}
    @media (max-width: 800px) {{ .storyboard-grid-5 {{ grid-template-columns: repeat(2, 1fr); }} }}
    @media (max-width: 500px) {{ .storyboard-grid-5 {{ grid-template-columns: 1fr; }} }}

    .beat-card-apple {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
      transition: transform 0.25s var(--apple-spring), border-color 0.2s, box-shadow 0.25s;
    }}
    .beat-card-apple:hover {{
      transform: translateY(-5px);
      border-color: var(--cl-accent);
      box-shadow: 0 16px 36px rgba(26, 115, 232, 0.14);
    }}

    .beat-img-box {{
      position: relative;
      width: 100%;
      aspect-ratio: 9 / 16;
      background: #000;
      overflow: hidden;
      cursor: pointer;
    }}
    .beat-img-box img {{
      width: 100%; height: 100%; object-fit: cover;
      transition: transform 0.4s ease;
    }}
    .beat-card-apple:hover .beat-img-box img {{
      transform: scale(1.05);
    }}
    .beat-badge {{
      position: absolute; top: 10px; left: 10px;
      background: rgba(0, 0, 0, 0.75); backdrop-filter: blur(8px);
      color: #fff; font-size: 10px; font-weight: 700;
      padding: 3px 8px; border-radius: 6px;
    }}
    .beat-time {{
      position: absolute; top: 10px; right: 10px;
      background: rgba(26, 115, 232, 0.9);
      color: #fff; font-family: 'JetBrains Mono', monospace;
      font-size: 10px; font-weight: 700;
      padding: 3px 8px; border-radius: 6px;
    }}

    .beat-content {{
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }}
    .beat-title {{ font-size: 14.5px; font-weight: 800; color: var(--cl-text-main); line-height: 1.35; }}
    .beat-voice {{
      font-size: 12px; font-weight: 600; color: #b45309; background: #fffbeb;
      padding: 6px 10px; border-radius: 6px; border-left: 3px solid #f59e0b; line-height: 1.5;
    }}
    .beat-specs {{
      width: 100%; font-size: 11px; border-collapse: collapse; margin-top: 4px;
    }}
    .beat-specs tr {{ border-bottom: 1px solid rgba(0, 0, 0, 0.05); }}
    .beat-specs tr:last-child {{ border-bottom: none; }}
    .beat-specs td {{ padding: 3px 0; }}
    .spec-label {{ color: var(--cl-text-muted); font-weight: 600; width: 42%; }}
    .spec-val {{ color: var(--cl-text-sub); font-weight: 700; }}
    .director-tip {{
      font-size: 11.5px; color: var(--cl-text-sub); background: var(--cl-bg-tint);
      padding: 8px 10px; border-radius: 8px; border: 1px solid var(--cl-border); line-height: 1.5; margin-top: auto;
    }}

    /* Reshoot Suggestions */
    .reshoot-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
      margin-top: 24px;
    }}
    @media (max-width: 860px) {{ .reshoot-grid {{ grid-template-columns: 1fr; }} }}

    .reshoot-card {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 16px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
    }}
    .reshoot-icon {{ font-size: 24px; }}
    .reshoot-title {{ font-size: 15px; font-weight: 800; color: var(--cl-text-main); }}
    .reshoot-desc {{ font-size: 13.5px; color: var(--cl-text-sub); line-height: 1.6; }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed; inset: 0; z-index: 999;
      background: rgba(0, 0, 0, 0.88); backdrop-filter: blur(16px);
      display: none; align-items: center; justify-content: center;
      padding: 24px;
    }}
    .lightbox-modal.active {{ display: flex; }}
    .lightbox-wrap {{
      max-width: 900px; width: 100%; max-height: 92vh;
      display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
      background: #111827; border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 20px; overflow: hidden; padding: 20px; color: #fff;
    }}
    @media (max-width: 768px) {{
      .lightbox-wrap {{ grid-template-columns: 1fr; max-height: 85vh; overflow-y: auto; }}
    }}
    .lightbox-img-box {{
      width: 100%; aspect-ratio: 9 / 16; max-height: 70vh;
      background: #000; border-radius: 12px; overflow: hidden;
    }}
    .lightbox-img-box img {{ width: 100%; height: 100%; object-fit: cover; }}
    .lightbox-info {{ display: flex; flex-direction: column; gap: 12px; justify-content: center; }}
    .lightbox-close {{
      align-self: flex-end; background: rgba(255, 255, 255, 0.1); border: none;
      color: #fff; width: 32px; height: 32px; border-radius: 50%; cursor: pointer; font-size: 16px;
    }}

    /* Toast */
    .toast {{
      position: fixed; bottom: 24px; right: 24px; z-index: 1000;
      background: #10b981; color: #fff; font-weight: 700; font-size: 13px;
      padding: 10px 18px; border-radius: 8px; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
      display: none; transform: translateY(10px); transition: all 0.3s ease;
    }}
    .toast.show {{ display: block; transform: translateY(0); }}
  </style>
</head>
<body>

  <!-- STICKY TOP NAV -->
  <header class="sticky-nav">
    <a href="lopmarketingbaitap.html" class="nav-brand">
      <span class="brand-badge">FEDU COURSE</span>
      <span class="nav-title">Bài tập {id}: {title}</span>
    </a>
    <div class="nav-actions">
      <a href="lopmarketingbaitap.html" class="nav-link-btn">← Trang tổng 12 bài tập</a>
      <select class="nav-select" onchange="if(this.value) window.location.href=this.value;">
        {nav_options}
      </select>
    </div>
  </header>

  <!-- KHỐI 1: HERO & VOICE-OVER CỐT LÕI (LIGHT) -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-hero">
    <div class="cl-container apple-reveal">
      <div class="hero-split">
        <div>
          <span class="cl-badge">BÀI TẬP THỰC HÀNH {id} / 12 • LỚP MARKETING PT</span>
          <h1 class="title-short">{title}</h1>
          <p class="editorial-quote">"Trạng thái tâm lý chủ đạo: {state}"</p>
          <p class="cl-lead">
            Thực hành ngay tại bàn học: băm nhỏ một hành động bình thường thành 5 cỡ cảnh và góc máy khác nhau.
            Khi mắt nhìn thấy chi tiết, tai nghe thấy nhịp thở, video tự khắc chạm vào lòng người mà không cần gồng mình diễn xuất.
          </p>

          <div class="voice-action-card">
            <div class="voice-head">
              <span class="voice-badge">🎙️ Kịch bản Voice-Over ngầm (Khớp 5 cú máy)</span>
              <button class="copy-voice-btn" onclick="copyVoiceText()">
                <span>Sao chép kịch bản</span>
              </button>
            </div>
            <div class="voice-text-box" id="voice-text">
              "{voice}"
            </div>
          </div>
        </div>

        <div>
          <div class="hero-avatar-box">
            <img src="{avatar}" alt="{title}" loading="lazy">
            <div class="hero-avatar-badge">
              <div class="avatar-tag">Trang phục thực chiến</div>
              <div class="avatar-name">Anh Việt • {outfit}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- KHỐI 2: BÓC TÁCH 4 TẦNG SỰ THẬT (TINT) -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-truth">
    <div class="cl-container apple-reveal">
      <span class="cl-badge">02 / BẢN ĐỒ TÂM LÝ HỌC HÀNH VI</span>
      <h2 class="title-long">Bóc Tách 4 Tầng Nhận Thức Khi Quay Cảnh Này</h2>
      <p class="cl-lead">Mỗi khung hình sinh ra đều mang một trọng lượng tâm lý. Đừng quay bề nổi, hãy chạm vào sự giằng xé bên trong người lớn.</p>

      <div class="tiers-grid">
        <div class="tier-apple-card t1">
          <div class="tier-label">Tầng 1 • Nói đãi bôi (Safe)</div>
          <div class="tier-desc">"{t1}"</div>
          <div class="tier-subnote">Lý do bề nổi: cái cớ an toàn ai cũng nói được để lấp liếm.</div>
        </div>
        <div class="tier-apple-card t2">
          <div class="tier-label">Tầng 2 • Cảm giác thật (Real)</div>
          <div class="tier-desc">"{t2}"</div>
          <div class="tier-subnote">Hành vi thật: thao tác vụng về đời thường diễn ra trước mắt.</div>
        </div>
        <div class="tier-apple-card t25">
          <div class="tier-label">Tầng 2.5 • Thể diện người lớn (Friction)</div>
          <div class="tier-desc">"{t25}"</div>
          <div class="tier-subnote">Giằng xé nội tâm: sợ bị người ngoài đánh giá làm màu hoặc thiếu chuyên nghiệp.</div>
        </div>
        <div class="tier-apple-card t3">
          <div class="tier-label">Tầng 3 • Tim đen ngượng miệng (Raw)</div>
          <div class="tier-desc">"{t3}"</div>
          <div class="tier-subnote">Nỗi bất an sâu thẳm: điểm nghẽn cốt tử khiến người ta dừng lại xem video.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- KHỐI 3: CHI TIẾT 5 CÚ MÁY PHÂN CẢNH (LIGHT) -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-storyboard">
    <div class="cl-container apple-reveal">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
        <div>
          <span class="cl-badge">03 / STORYBOARD STUDIO 9:16</span>
          <h2 class="title-long">5 Cú Máy Băm Cảnh Trám Đổi 3 Trục</h2>
        </div>
        <span style="font-size: 12px; color: var(--cl-text-muted);">Bấm vào ảnh để xem chi tiết góc máy đạo diễn</span>
      </div>

      <div class="storyboard-grid-5">
        {beats_html}
      </div>
    </div>
  </section>

  <!-- KHỐI 4: GỢI Ý BỐI CẢNH QUAY LẠI (TINT) -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-reshoot">
    <div class="cl-container apple-reveal">
      <span class="cl-badge">04 / BÀI TẬP VỀ NHÀ THỰC CHIẾN</span>
      <h2 class="title-long">3 Bối Cảnh Thực Tế Để Quay Lại Khi Rời Lớp Học</h2>
      <p class="cl-lead">Khi đã nắm chắc phản xạ băm nhỏ 5 cỡ cảnh tại lớp, học viên có thể xách máy ra quay lại ở bất kỳ không gian nào dưới đây.</p>

      <div class="reshoot-grid">
        {reshoot_html}
      </div>
    </div>
  </section>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-modal" id="lb-modal" onclick="closeLightbox(event)">
    <div class="lightbox-wrap" onclick="event.stopPropagation()">
      <div class="lightbox-img-box">
        <img id="lb-img" src="" alt="Frame Detail">
      </div>
      <div class="lightbox-info">
        <button class="lightbox-close" onclick="closeLightbox()">✕</button>
        <span class="cl-badge" id="lb-time">00:00 - 02.5s</span>
        <h3 id="lb-title" style="font-size: 18px; font-weight: 800;">Tiêu đề</h3>
        <div class="beat-voice" id="lb-voice" style="margin: 8px 0;">Lời thoại</div>
        <div class="director-tip" id="lb-tip" style="background: rgba(255,255,255,0.06); color:#cbd5e1;">Mẹo</div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast-msg">Đã sao chép kịch bản voice-over!</div>

  <script>
    // Copy Voiceover text
    function copyVoiceText() {{
      const text = document.getElementById('voice-text').innerText.replace(/^"|"$/g, '').trim();
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast-msg');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2200);
      }});
    }}

    // Lightbox functions
    function openLightbox(imgSrc, title, time, voice, tip) {{
      document.getElementById('lb-img').src = imgSrc;
      document.getElementById('lb-title').innerText = title;
      document.getElementById('lb-time').innerText = time;
      document.getElementById('lb-voice').innerText = '🎙️ ' + voice;
      document.getElementById('lb-tip').innerHTML = '💡 <b>Mẹo Ông Giáo:</b> ' + tip;
      document.getElementById('lb-modal').classList.add('active');
    }}

    function closeLightbox() {{
      document.getElementById('lb-modal').classList.remove('active');
    }}

    // Apple reveal animation on scroll
    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('is-visible');
        }}
      }});
    }}, {{ threshold: 0.1 }});

    document.querySelectorAll('.apple-reveal').forEach(el => observer.observe(el));
  </script>
</body>
</html>
"""

def build_all():
    base_dir = '/Users/vietmac/Documents/CODE/course'
    
    # 1. Generate nav options
    for ex in EXERCISES:
        ex_id = ex["id"]
        slug = ex["slug"]
        
        # Build nav dropdown
        nav_opts = []
        for other in EXERCISES:
            sel = "selected" if other["id"] == ex_id else ""
            nav_opts.append(f'<option value="{other["slug"]}" {sel}>Bài {other["id"]}: {other["title"][:28]}...</option>')
        nav_options_html = "\n        ".join(nav_opts)
        
        # Build beats html
        beats_blocks = []
        for idx, (b_title, b_time, b_size, b_angle, b_dir, b_voice, b_tip) in enumerate(ex["shots"], 1):
            img_path = f'{ex["frame_dir"]}/shot{idx}.jpg'
            b_html = f"""
        <div class="beat-card-apple">
          <div class="beat-img-box" onclick="openLightbox('{img_path}', '{idx}. {b_title}', '{b_time}', '{b_voice}', '{b_tip}')">
            <img src="{img_path}" alt="{b_title}" loading="lazy">
            <span class="beat-badge">{b_size}</span>
            <span class="beat-time">{b_time}</span>
          </div>
          <div class="beat-content">
            <div class="beat-title">{idx}. {b_title}</div>
            <div class="beat-voice">🎙️ "{b_voice}"</div>
            <table class="beat-specs">
              <tr><td class="spec-label">Cỡ cảnh</td><td class="spec-val">{b_size}</td></tr>
              <tr><td class="spec-label">Góc máy</td><td class="spec-val">{b_angle}</td></tr>
              <tr><td class="spec-label">Hướng</td><td class="spec-val">{b_dir}</td></tr>
            </table>
            <div class="director-tip">💡 <b>Mẹo Ông Giáo:</b> {b_tip}</div>
          </div>
        </div>"""
            beats_blocks.append(b_html)
        beats_html = "\n".join(beats_blocks)
        
        # Build reshoot html
        reshoot_blocks = []
        icons = ["☕", "🏢", "🌳"]
        for idx, (r_title, r_desc) in enumerate(ex["reshoots"]):
            icon = icons[idx % len(icons)]
            r_html = f"""
        <div class="reshoot-card">
          <div class="reshoot-icon">{icon}</div>
          <div class="reshoot-title">{r_title}</div>
          <div class="reshoot-desc">{r_desc}</div>
        </div>"""
            reshoot_blocks.append(r_html)
        reshoot_html = "\n".join(reshoot_blocks)
        
        page_html = TEMPLATE.format(
            id=ex["id"],
            title=ex["title"],
            state=ex["state"],
            outfit=ex["outfit"],
            avatar=ex["avatar"],
            voice=ex["voice"],
            t1=ex["t1"],
            t2=ex["t2"],
            t25=ex["t25"],
            t3=ex["t3"],
            nav_options=nav_options_html,
            beats_html=beats_html,
            reshoot_html=reshoot_html
        )
        
        out_file = os.path.join(base_dir, slug)
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(page_html)
        print(f"Built {slug} successfully!")

if __name__ == '__main__':
    build_all()
