public class BinaryTree_search {

    public static class TreeNode {
        private TreeNode left, right;
        private String data;

        public TreeNode(String data) { this.data = data; }

        public void setLeft(TreeNode node) { left = node; }
        public void setRight(TreeNode node) { right = node; }
        public void setData(String data) { this.data = data; }

        public TreeNode getLeft() { return left; }
        public TreeNode getRight() { return right; }
        public String getdata() { return data; }
    }

    public static void SearchBinarytree(String findData, TreeNode node) {
        if (findData == node.data) {
            System.out.printf("%s 을(를) 찾았습니다.\n", node.data);
        } 
        else if (findData.charAt(0) < node.data.charAt(0)
            && node.left != null) {
            SearchBinarytree(findData, node.left);
        } 
        else if (findData.charAt(0) > node.data.charAt(0)
            && node.right != null) {
            SearchBinarytree(findData, node.right);
        } else {
            System.out.printf("%s 을(를) 찾지 못 하였습니다.\n", findData);
        }
    }

    public static void setBinarytree(TreeNode root, String data) {
        if(data.charAt(0) < root.data.charAt(0)) {
            if (root.left==null) {
                root.left = new TreeNode(data);
                return;
            }
            setBinarytree(root.left, data);
        } else {
            if (root.right==null) {
                root.right = new TreeNode(data);
                return;
            }
            setBinarytree(root.right, data);
        }
    }

    public static TreeNode UpdateNode(String MinData, String MaxData, TreeNode node) {
        TreeNode subRight = node.right;
        TreeNode subLeft = node.left;

        if (subLeft == null && subRight == null) {
            return node;
        }
        else if (subRight == null) {
            return subLeft;
        }
        else if (subLeft == null) {
            return subRight;
        }
        else if (subRight.left != null) {
            return UpdateNode(subLeft.data, subRight.data, node.right);
        } else {
            return UpdateNode(node.left.data, node.right.data, node.left);
        }
    }
    
    public static TreeNode deleteBinarytree(String deleteData, TreeNode root) {
        TreeNode node = root;
        TreeNode superNode = node;

        while (node.data != deleteData) {
            superNode = node;
            if (deleteData.charAt(0) < node.data.charAt(0) && node.left != null) {
                node = node.left;
            } else if (deleteData.charAt(0) > node.data.charAt(0) && node.right != null) {
                node = node.right;
            } else {
                System.out.println(deleteData + "는(은) 찾을 수 없습니다.");
                return root;
            }
        }
        
        TreeNode subRight = node.right;
        TreeNode subLeft = node.left;

        node = UpdateNode(subLeft.data, subRight.data, node);

        // ※ UpdateNode로 가져온 노드가 자식노드에 남아져 있으므로 무한 복사가 이루어짐
        if (node != subLeft) { node.left = subLeft; }
        if (node != subRight) { node.right = subRight; }

        if (superNode.left.data == deleteData) { superNode.left = node; } 
        else { superNode.right = node; }
        System.out.println(deleteData + "를(을) 성공적으로 삭제하였습니다.");
        return superNode;
    }

    // public static void main(String[] args) {
    //     String[] name_ary = new String[] {
    //         "블랙핑크",
    //         "레드벨벳",
    //         "마마무",
    //         "에이핑크",
    //         "걸스데이",
    //         "트와이스"
    //     };

    //     TreeNode root = new TreeNode(name_ary[0]);
    //     for (int i = 1; i < name_ary.length; i++) {
    //         setBinarytree(root, name_ary[i]);
    //     }

    //     SearchBinarytree("트와이스", root);

    //     deleteBinarytree("레드벨벳", root);
    //     SearchBinarytree("레드벨벳", root);
    // }

    public static void main(String[] args) {
        // ABCDEFGHIJKLMNOPQRSTUVWXYZ
        String[] name_ary = new String[] {
            "MM", "NN",
            "FF", "SS",
            "CC", "HH", "WW", "PP",
            "QQ", "OO", "GG", "AA",
            "II", "XX"
        };

        TreeNode root = new TreeNode(name_ary[0]);
        for (int i = 1; i < name_ary.length; i++) {
            setBinarytree(root, name_ary[i]);
        }
        
        System.out.println("\n#####################\n");
        for (int i = 1; i < name_ary.length; i++) {
            SearchBinarytree(name_ary[i], root);
        }
        System.out.println("\n#####################\n");

        root = deleteBinarytree("FF", root);
        SearchBinarytree("FF", root);

        System.out.println("\n#####################\n");

        for (int i = 1; i < name_ary.length; i++) {
            SearchBinarytree(name_ary[i], root);
        }
    }
}
