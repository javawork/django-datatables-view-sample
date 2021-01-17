$(document).ready(function () {

    // 選択中のレコードid
    let selected = [];

    // DataTables 設定
    // https://datatables.net/reference/index
    let table = $('#datatable').DataTable({

        // Server-side processing:Ajaxモードの設定
        // https://datatables.net/examples/server_side/simple.html
        processing: true,
        serverSide: true,
        ajax: "./items",

        // dom: 検索フィールド等の各種ウィジェットの配置
        // https://datatables.net/reference/option/dom
        // dom: 'lfrtip',

        // lengthMenu: １ページに表示させる件数のリスト
        // https://datatables.net/reference/option/lengthMenu
        lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "All"]],

        // pageLength: pageLengthの初期値
        // https://datatables.net/reference/option/pageLength
        pageLength: 10,

        // language: 表示メッセージのローカライズ
        // https://datatables.net/reference/option/language
        // 日本語版ソース:https://github.com/DataTables/Plugins/blob/master/i18n/Japanese.lang
        language: {
            "thousands": ",",
            "sProcessing": "Processing...",
            "sLengthMenu": "_MENU_ count",
            "sZeroRecords": "no data",
            "sInfo": "_START_ ～ _END_ Show from _TOTAL_ ",
            "sInfoEmpty": "empty",
            "sInfoFiltered": "From Total _MAX_ data）",
            "sInfoPostFix": "",
            "sSearch": "Search:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<<",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": ">>"
            },
        },
        // rowCallback: 行の描画時に追加処理を行いたいときに使う。
        // https://datatables.net/reference/option/rowCallback

        // ページ遷移時に選択済みの行の表示を変更している。
        rowCallback: function (row, data) {
            $(row).attr('data-id', data[0]);
            if ($.inArray(data[0], selected) !== -1) {
                $(row).addClass('selected');
            }
        },

        // columns: 列の設定
        // https://datatables.net/reference/option/columns

        // 列の設定は 'columns' または 'columnDefs' で行う。
        // columns のほうが冗長な記述になるが視認性が良い気がする。

        // BaseDatatableViewのcolumnsの設定順にフィールドが列に割り当てられる。
        // columnsのフィールド数より列数が少ないとエラーになるので注意。

        // columnsと実際の列表示の内容を変更したい場合は以下のオプションで工面するとよい。

        // visible: bool    列の表示/非表示
        // data: number     違う列のデータを表示
        // render: function 関数でデータを加工

        // render内で他の列のデータを使うこともできる。
        // https://datatables.net/manual/data/renderers

        columns: [
            {
                // 1列目(id)
                title: "&nbsp;",
                className: 'select-checkbox',
                searchable: false,
                render: function () {
                    return "";
                },
            },
            {
                title: "Name",
                visible: true,
                searchable: true,
            },
            {
                title: "Position",
                visible: true,
                searchable: true,
            },
            {
                title: "Age",
                visible: false,
                searchable: false,
            },
            {
                title: "Team",
                visible: true,
                searchable: true,
            },
            {
                title: "G",
                visible: false,
                searchable: false,
            },
            {
                title: "GS",
                visible: false,
                searchable: false,
            },
            {
                title: "MP",
                visible: false,
                searchable: false,
            },
            {
                title: "FG",
                visible: false,
                searchable: false,
            },
            {
                title: "FGA",
                visible: false,
                searchable: false,
            },
            {
                title: "FG%",
                visible: true,
                searchable: false,
            },
            {
                title: "3P",
                visible: false,
                searchable: false,
            },
            {
                title: "3PA",
                visible: false,
                searchable: false,
            },
            {
                title: "3P%",
                visible: true,
                searchable: false,
            },
            {
                title: "2P",
                visible: false,
                searchable: false,
            },
            {
                title: "2PA",
                visible: false,
                searchable: false,
            },
            {
                title: "2P%",
                visible: false,
                searchable: false,
            },
            {
                title: "FT",
                visible: false,
                searchable: false,
            },
            {
                title: "FTA",
                visible: false,
                searchable: false,
            },
            {
                title: "FT%",
                visible: false,
                searchable: false,
            },
            {
                title: "ORB",
                visible: false,
                searchable: false,
            },
            {
                title: "DRB",
                visible: false,
                searchable: false,
            },
            {
                title: "TRB",
                visible: true,
                searchable: false,
            },
            {
                title: "AST",
                visible: true,
                searchable: false,
            },
            {
                title: "STL",
                visible: true,
                searchable: false,
            },
            {
                title: "BLK",
                visible: true,
                searchable: false,
            },
            {
                title: "TOV",
                visible: false,
                searchable: false,
            },
            {
                title: "PF",
                visible: false,
                searchable: false,
            },
            {
                title: "PTS",
                visible: true,
                searchable: false,
            },
        ],
    });


    // server-side利用時は拡張機能の選択(Select)が使えないので、DataTables公式の
    // サンプルコードを元に選択処理を自作する。
    // https://datatables.net/examples/server_side/select_rows.html
    $('#datatable tbody').on('click', 'tr', function () {

        selected = [];
        $('#datatable tr').removeClass('selected');
        $('#selected').html(selected.join(','))

        let id = $(this).attr('data-id');
        let index = $.inArray(id, selected);

        if (index === -1) {

            selected.push(id);
            selected.sort(function (a, b) {
                return a - b
            });
            $(this).addClass('selected');
        } else {
            selected.splice(index, 1);
            $(this).removeClass('selected');
        }
        $('#selected').html(selected.join(','));
    });

    // サンプル：クリックしたレコードのデータを取得
    // data()でセル、行、表示中のテーブル全体のデータを取得可能
    // https://datatables.net/reference/api/row().data()

    $('#datatable tbody').on('click', 'tr', function () {
        console.log(table.row(this).data());
    });

    // 全選択を解除
    $('#clear').on('click', function () {
        selected = [];
        $('#datatable tr').removeClass('selected');
        $('#selected').html(selected.join(','))
    })

    // 印刷・Excel・CSVボタン クリック
    $('.report').on('click', function () {

        if (selected.length == 0) {
            alert('먼저 데이터를 선택하세요');
            return false;
        }

        // 隠しフォームに選択したidを格納し、各機能のWebAPIに送信する
        let form = $("#form")[0];
        $("*[name=id_list]").val(selected.join('_'))
        form.method = 'GET';

        // GETクエリの長さ制限に注意。このコードは大量件数の選択に配慮していません。
        // https://support.microsoft.com/ja-jp/help/208427/maximum-url-length-is-2-083-characters-in-internet-explorer

        // ボタンのidで処理判定
        switch (this.id) {
            case
            'print':
                // 印刷のみ別ウィンドウを開く
                window.open('', 'new_window');
                form.action = 'print';
                form.target = 'new_window';
                form.submit();
                break;
            case
            'excel':
                form.action = 'excel';
                form.submit();
                break;
            case
            'csv':
                form.action = 'csv';
                form.submit();
                break;
        }
    })
});