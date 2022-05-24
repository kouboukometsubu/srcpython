import os
import shutil
import pathlib
import glob
from send2trash import send2trash

# <summary>
# プロジェクト名（アセンブリ名）を取得
# </summary>
# <returns></returns>
def GetProjectName():
    return("test")

# <summary>
# フルパスからファイル名を抽出
# </summary>
# <param name="pFullPath"></param>
# <returns></returns>
def GetFileName(FullPath):
    # ファイル名 を取得する
    stParentName = os.path.basename(FullPath)
    return (stParentName)
    
# <summary>
# フルパスからディレクトリだけ抜き出す
# </summary>
# <param name="pFullPath"></param>
# <returns></returns>
def GetFilePath(FullPath):
    # 親ディレクトリ名 (フォルダ名) を取得する
    stParentName = os.path.dirname( FullPath )
    return(stParentName)


def CreateDirectory( folder ):
    os.makedirs(folder)

def CreateFolder( folder ):
    os.makedirs(folder)

# フォルダ内のファイル数を数える
def GetFileCountInFolder( foldername ):
	files = glob.glob(foldername + "*.*")
	return( files.count)

#MakeDirectoryAll( string filename )				    # ディレクトリを自動作成

def IsExistDirectory( dirname):				# フォルダの存在確認
	ret = IsDirectory(dirname)
	return (ret)

def CheckExistDirectoryAndCreate(  directory ):
	if IsExistDirectory( directory) == False:
		rc = CreateFolder(directory)
		if rc != 0:
			return (-1)
		else:
			return( 0 )
	return( 0 ) 

   


# ファイルの存在確認
def IsExistFile(filename):					
    ret = os.path.isfile(filename)
    return (ret)
    

def IsFile( path ):
	ret = IsExistFile(path)
	return (ret)


def IsDirectory( path ):
	ret = os.path.isdir(path)
	return (ret)

def CopyFile(src, dst):				# ファイルをコピーする
	shutil.copyfile(src, dst)

def DeleteFile(filename):						# ファイルを消す
	os.remove(filename)

def MoveToTrash( filename, bMessage ):	# ゴミ箱へファイルを移動
	File.Delete(filename )

def DeleteFileInFolder( folder_name ): 			# フォルダ内のファイルを全て削除
	files = glob.glob(folder_name + "\*.*")
	
	for item in files:
		DeleteFile(item)

		
"""
        public static string GetCurrentDirectory() 
        {
#if FRAME_WORK_4
            return (Application.StartupPath); 
#else
            System.Reflection.Assembly assembly = System.Reflection.Assembly.GetEntryAssembly();

            string exeName = assembly.Location;

            string path = GetFilePath( exeName ) ;

            return (path); 
#endif
            #return (System.IO.Directory.GetCurrentDirectory());
        }
"""

# 2005.11.15
# 拡張子（ピリオドを含む)を取得
def GetExtension(pFullPath):
	#string stParentName = Path.GetExtension(pFullPath);
	root, ext = os.path.splitext(pFullPath)
	return ("." + ext)

# ピリオドなし拡張子取得
def GetExtensionNotPiriod( pFullPath):
	#string stParentName = Path.GetExtension(pFullPath);
	root, ext = os.path.splitext(pFullPath)
	return ( ext)

# 拡張子なしファイル名取得
def GetFilenameWithoutExtention(pFullPath):
	filename = GetFilename( pFullPath)
	root, ext = os.path.splitext(filename)
	return( root )


"""
    # 2006.01.22
#	    static int Replace( string filename, string Pre, string Next ) 

        public static void CopyFileInFolder(string FolderSrc, string FolderDst/*, CTakanoThread* pThread = NULL*/)
        {
            CopyDirectory(FolderSrc, FolderDst);
        }


        # <summary>
        # ディレクトリをコピーする
        # </summary>
        # <param name="sourceDirName">コピーするディレクトリ</param>
        # <param name="destDirName">コピー先のディレクトリ</param>
        public static void CopyDirectory(
            string sourceDirName, string destDirName)
        {
            #コピー先のディレクトリがないときは作る
            if (!System.IO.Directory.Exists(destDirName))
            {
                System.IO.Directory.CreateDirectory(destDirName);
                #属性もコピー
                System.IO.File.SetAttributes(destDirName,
                    System.IO.File.GetAttributes(sourceDirName));
            }

            #コピー先のディレクトリ名の末尾に"\"をつける
            if (destDirName[destDirName.Length - 1] !=
                    System.IO.Path.DirectorySeparatorChar)
                destDirName = destDirName + System.IO.Path.DirectorySeparatorChar;

            #コピー元のディレクトリにあるファイルをコピー
            string[] files = System.IO.Directory.GetFiles(sourceDirName);
            foreach (string file in files)
                System.IO.File.Copy(file,
                    destDirName + System.IO.Path.GetFileName(file), true);

            #コピー元のディレクトリにあるディレクトリについて、再帰的に呼び出す
            string[] dirs = System.IO.Directory.GetDirectories(sourceDirName);
            foreach (string dir in dirs)
                CopyDirectory(dir, destDirName + System.IO.Path.GetFileName(dir));
        }
        
        
#	    static bool IsSameFile( string FileSrc, string FileDst )

    # 2007.02.16
#	    static void CreateFile( string FileName ) 

    # 2007.02.22
	    public static DateTime GetFileMakeTime( string FileName )
		{
			DateTime ret = File.GetCreationTime(FileName);

			return (ret);

		}
		
		public static DateTime GetFileLastWriteTime( string FileName )
		{
			DateTime ret = File.GetLastWriteTime(FileName);

			return (ret);

		}

    # 2009.02.13
		public static bool CompFileLastWriteTime(string FileSrc, string FileDst)
		{
			DateTime retSrc = File.GetLastWriteTime(FileSrc);
			DateTime retDst = File.GetLastWriteTime(FileDst);

			bool ret = retSrc > retDst;

			return (ret);
		}
	    public static string GetAppName()
		{
			string str = "";

			
			string appPath; #アプリケーションのファイルパス
			string appFileName; #アプリケーションのファイル名
			string appName; #アプリケーションの拡張子を取り除いたアプリケーション名

			#パスの取得
#if FRAME_WORK_4
 			appPath = Application.ExecutablePath;
#else
			appPath = GetCurrentDirectory() ;#.ExecutablePath;
#endif
			#アプリケーションのファイル名
			appFileName = Path.GetFileName(appPath);


			#拡張子を除いたアプリケーションファイル名
			appName = Path.ChangeExtension(appFileName, null);

			return (appName);
		}

		public static string GetFileVersion()
		{
#if FRAME_WORK_4
 			string appPath = Application.ExecutablePath;
#else
            string appPath = GetCurrentDirectory();#.ExecutablePath;
#endif		
            #string appPath = Application.ExecutablePath; 

			# 指定したファイルのバージョン情報を取得する
			FileVersionInfo hVerInfo = FileVersionInfo.GetVersionInfo(appPath);

			return (hVerInfo.FileVersion);
		}


		# ファイルをバックアップする
		# test.csv ==> test20170102102010.csv
		public static int BackupFile( string fullpath, string backupFolder )
		{

			int rc1 = CheckExistDirectoryAndCreate(backupFolder);
			if ( rc1 != 0 )
			{
				return (-1);
			}

			string newFilename = CreateBackupFileName(fullpath, backupFolder);

			int rc2 = CopyFile(fullpath, newFilename);
			if ( rc2 !=  0)
			{
				return (-2);
			}

			return ( 0 );
		}


		# バックアップファイル名を作成する
		public static string CreateBackupFileName( string fullpath, string backupDirectory 
#if FRAME_WORK_4
            = ""
#endif
            )
		{
			string appFileName; #アプリケーションのファイル名
			string appName; #アプリケーションの拡張子を取り除いたアプリケーション名

			string folder = Path.GetDirectoryName(fullpath);

			if (backupDirectory != "")
			{
				folder = backupDirectory;
			}

			#アプリケーションのファイル名
			appFileName = Path.GetFileName(fullpath);

			#拡張子を除いたアプリケーションファイル名
			appName = Path.ChangeExtension(appFileName, null);

			string strTime = TakanoTime.GetCurrentTimeStringSimple() ;

			string strExt = GetExtension(fullpath);

			string ret = folder + "\\" + appName + strTime + strExt ;

			return( ret ) ;

		}
"""

# 拡張子を変更したファイル名を取得
def ChangeExtension( fullpath, newExtention ):
	filename = pathlib.PurePath(fullpath).stem
    #sf = pathlib.PurePath(fullpath).suffix
	# 変更後のファイル名を得る
	new_filename = filename + newExtention
	return( new_filename )

#ファイル名の最後に文字列を追加したファイル名を取得
def AddStrTailOfFileName( fullpath, strAdd ):
	# ファイルの拡張子を得る
	strExt = pathlib.PurePath(fullpath).suffix
	# ファイル名(拡張子除く)を得る
	filename = pathlib.PurePath(fullpath).stem
	ret = filename + strAdd + strExt
	return (ret)



if __name__ == '__main__':
    print("これは自作モジュールです")